from digestiflow_demux.snakemake_support import get_result_files_demux
from tests.flowcell_config import return_config1


def test_get_output_files_demux(mocker):
    expected = [
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L001/5346_S1_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L002/5346_S1_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L003/5346_S1_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L004/5346_S1_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L001/5347_S2_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L002/5347_S2_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L003/5347_S2_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L004/5347_S2_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L001/5348_S3_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L002/5348_S3_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L003/5348_S3_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L004/5348_S3_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L001/5349_S4_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L002/5349_S4_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L003/5349_S4_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L004/5349_S4_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L001/5350_S5_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L002/5350_S5_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L003/5350_S5_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L004/5350_S5_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L001/5351_S6_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L002/5351_S6_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L003/5351_S6_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L004/5351_S6_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L001/5352_S7_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L002/5352_S7_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L003/5352_S7_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L004/5352_S7_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L001/5353_S8_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L002/5353_S8_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L003/5353_S8_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L004/5353_S8_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L001/5354_S9_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L002/5354_S9_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L003/5354_S9_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L004/5354_S9_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L001/5355_S10_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L002/5355_S10_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L003/5355_S10_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L004/5355_S10_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L001/5356_S11_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L002/5356_S11_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L003/5356_S11_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L004/5356_S11_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L001/5357_S12_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L002/5357_S12_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L003/5357_S12_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L004/5357_S12_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L001/Undetermined_S0_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L002/Undetermined_S0_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L003/Undetermined_S0_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L004/Undetermined_S0_L004_R1_001.fastq.gz',
    ]
    mocker.patch('digestiflow_demux.snakemake_support.config_to_rta_version', return_value=(2, 0, 0))
    files = get_result_files_demux(return_config1())
    assert files == expected


def test_get_output_files_demux_RTAv1(mocker):
    expected = [
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L001/5346_CAAAAG_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L002/5346_CAAAAG_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L003/5346_CAAAAG_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5346/HLVHXXXXX/L004/5346_CAAAAG_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L001/5347_CAACTA_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L002/5347_CAACTA_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L003/5347_CAACTA_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5347/HLVHXXXXX/L004/5347_CAACTA_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L001/5348_CACCGG_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L002/5348_CACCGG_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L003/5348_CACCGG_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5348/HLVHXXXXX/L004/5348_CACCGG_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L001/5349_CACGAT_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L002/5349_CACGAT_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L003/5349_CACGAT_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5349/HLVHXXXXX/L004/5349_CACGAT_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L001/5350_CACTCA_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L002/5350_CACTCA_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L003/5350_CACTCA_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5350/HLVHXXXXX/L004/5350_CACTCA_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L001/5351_CAGGCG_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L002/5351_CAGGCG_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L003/5351_CAGGCG_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5351/HLVHXXXXX/L004/5351_CAGGCG_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L001/5352_CATGGC_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L002/5352_CATGGC_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L003/5352_CATGGC_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5352/HLVHXXXXX/L004/5352_CATGGC_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L001/5353_CATTTT_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L002/5353_CATTTT_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L003/5353_CATTTT_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5353/HLVHXXXXX/L004/5353_CATTTT_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L001/5354_CCAACA_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L002/5354_CCAACA_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L003/5354_CCAACA_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5354/HLVHXXXXX/L004/5354_CCAACA_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L001/5355_CGGAAT_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L002/5355_CGGAAT_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L003/5355_CGGAAT_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5355/HLVHXXXXX/L004/5355_CGGAAT_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L001/5356_CTAGCT_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L002/5356_CTAGCT_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L003/5356_CTAGCT_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5356/HLVHXXXXX/L004/5356_CTAGCT_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L001/5357_CTATAC_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L002/5357_CTATAC_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L003/5357_CTATAC_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/5357/HLVHXXXXX/L004/5357_CTATAC_L004_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L001/lane1_Undetermined_L001_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L002/lane2_Undetermined_L002_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L003/lane3_Undetermined_L003_R1_001.fastq.gz',
        '/output/210118_NB500000_0001_AHLVHXXXXX/Undetermined/HLVHXXXXX/L004/lane4_Undetermined_L004_R1_001.fastq.gz',
    ]
    mocker.patch('digestiflow_demux.snakemake_support.config_to_rta_version', return_value=(1, 0, 0))
    files = get_result_files_demux(return_config1())
    assert files == expected