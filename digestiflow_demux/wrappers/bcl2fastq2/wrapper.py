"""Snakemake wrapper for bcl2fastq2.

This file is part of Digestify Demux.
"""

import glob
import os
import sys
from snakemake import shell

# A hack is required for being able to import snappy_wrappers modules when in development mode.
# TODO: is there a more elegant way?
base_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, base_dir)

from digestiflow_demux.bases_mask import return_bases_mask  # noqa: E402
from digestiflow_demux.snakemake_support import build_sample_map  # noqa: E402

__author__ = "Manuel Holtgrewe <manuel.holtgrewe@bihealth.de>"

shell.executable("/bin/bash")

# Get number of barcode mismatches, defaults to 1 for bcl2fastq v2.
barcode_mismatches = snakemake.config.get("barcode_mismatches")  # noqa
if barcode_mismatches is None:
    barcode_mismatches = 1

# More than 8 threads will not work for bcl2fastq.
bcl2fastq_threads = min(64, snakemake.config["cores"])  # noqa

# Get bases mask for the current sample sheet
planned_reads = snakemake.config["flowcell"]["planned_reads"]  # noqa
bases_mask = os.path.basename(os.path.dirname(snakemake.input.sheet))  # noqa
bases_mask_illumina = return_bases_mask(planned_reads, bases_mask)

# Get sample map to get sample numbering correct
sample_map = build_sample_map(snakemake.config["flowcell"])  # noqa
sample_map["Undetermined"] = "S0"

# Get additional bcl2fastq2 parameters
add_params = ""
for arg, value in snakemake.config["bcl2fastq2_params"].items():  # noqa
    if value:
        if isinstance(value, bool):
            add_params += " --" + arg.replace("_", "-")
        elif isinstance(value, int):
            add_params += " --" + arg.replace("_", "-") + " " + str(value)

shell(
    r"""
set -euo pipefail
set -x

# -------------------------------------------------------------------------------------------------
# Setup Auto-cleaned Temporary Directory.

export TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

# -------------------------------------------------------------------------------------------------
# Print Sample Sheet

head -n 10000 {snakemake.input.sheet}

# -------------------------------------------------------------------------------------------------
# Execute bcl2fastq v2

bcl2fastq \
    --barcode-mismatches {barcode_mismatches} \
    --sample-sheet {snakemake.input.sheet} \
    --runfolder-dir {snakemake.params.input_dir} \
    --output-dir $TMPDIR/demux_out \
    --interop-dir $TMPDIR/interop_dir \
    --processing-threads {bcl2fastq_threads} \
    --use-bases-mask {bases_mask_illumina} \
    {add_params} {snakemake.params.tiles_arg}

ls -lhR $TMPDIR/demux_out

# -------------------------------------------------------------------------------------------------
# Move Files to Destination.

# Move sample FASTQ files.
flowcell={snakemake.params.flowcell_token}
srcdir=$TMPDIR/demux_out/Project

for path in $srcdir/*; do
    sample=$(basename $path | rev | cut -d _ -f 5- | rev)
    lane=$(basename $path | rev | cut -d _ -f 3 | rev)
    dest={snakemake.params.output_dir}/$sample/$flowcell/$lane/{bases_mask}__$(basename $path)
    mkdir -p $(dirname $dest)
    cp -dR $path $dest
done

# Move undetermined FASTQ files.
srcdir=$TMPDIR/demux_out

for path in $srcdir/Undetermined_*; do
    if [[ -f $path ]]; then
        lane=$(basename $path | rev | cut -d _ -f 3 | rev)
        dest={snakemake.params.output_dir}/Undetermined/$flowcell/$lane/{bases_mask}__$(basename $path)
        mkdir -p $(dirname $dest)
        cp -dR $path $dest
    fi
done

# Write out the html report files as an archive
srcdir=$TMPDIR/demux_out
pushd $srcdir
tar -czvf {snakemake.params.output_dir}/html_report_{bases_mask}.tar.gz Reports
popd

touch {snakemake.output.marker}
"""
)

# bcl2fastq2 starts to count samples from 0 for each run. This breaks snakemake's assumption that
# all samples from all sample sheets are numbered incrementally. Here, we look up the correct
# sample number and replace it in the path. Easier to do in python than in bash above.
fls = glob.glob(
    os.path.join(snakemake.params.output_dir, "*/*/*/" + bases_mask + "__*.fastq.gz")  # noqa
)
for path in fls:
    f = os.path.basename(path)
    name = f.split("__", 1)[1]  # remove $bases_mask__
    name_elements = name.split("_")[:-3]
    oldS = name_elements[-1]
    name = "_".join(name_elements[:-1])
    newS = sample_map[name]
    newpath = path.replace("_".join([name, oldS]), "_".join([name, newS]))
    os.rename(path, newpath)
