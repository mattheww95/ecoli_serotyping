import hashlib
import sys
import pytest
from ectyper import ectyper


def set_input(input, percent_iden=None, output=None):
    """
    Create the sys.argv[] without need for commandline input.
    :param input: Input file given by testing function
    :param percent_iden: Percent identity for comparison
    :param output: Location of output
    :return: None
    """
    args = ['-i', input]
    if percent_iden:
        args += ['-d', str(percent_iden)]
    if output:
        args += ['-o', output]
    sys.argv[1:] = args


def get_md5(file):
    """
    Get the md5sum for a file.
    :param file: The file to get an md5sum from.
    :return: The md5sum of the file
    """
    with open(file, 'rb') as handler:
        return hashlib.md5(handler.read()).hexdigest()


def test_integration_invalid_file():
    """
    Giving a non-fasta file in fasta-file name.
    :return: None
    """
    file = 'test/Data/test_dir/badfasta.fasta'
    set_input(file)
    with pytest.raises(SystemExit) as se:
        ectyper.run_program()
    assert se.type == SystemExit
    assert se.value.code == "No valid genomes"


def test_integration_no_file():
    """
    Giving no input to the program.
    :return: None
    """
    file = ''
    set_input(file)
    with pytest.raises(SystemExit) as se:
        ectyper.run_program()
    assert se.type == SystemExit
    assert se.value.code == "No valid genomes"


# def test_valid_fastq_file():
#     """
#     Given a valid fastq file, get the correct results.
#     Use a temp dir for the test output
#     :return: None
#     """
#     file = 'test/Data/Escherichia.fastq'
#     set_input(input, output=output_dir)
#     ectyper.run_program()

#     def test_folder_input(self):
#         input = 'test/Data/test_dir'
#         output_dir = 'test_folder_input'
#         set_input(input, output=output_dir)
#         expected_checksum = 'bd9354495c264bcfb79c5581b9e7c953'
#         ectyper.run_program()
#         self.assertEqual(
#             get_md5(os.path.join('output', output_dir, 'output.csv')),
#             expected_checksum
#         )
#
#     def test_list_input(self):
#         input = 'test/Data/test_dir/sample.fasta,test/Data/test_dir/sample.fasta'
#         output_dir = 'test_list_input'
#         set_input(input, output=output_dir)
#         expected_checksum = '3ad690bf9f3ea87dd0200600f72fa618'
#         ectyper.run_program()
#         self.assertEqual(
#             get_md5(os.path.join('output', output_dir, 'output.csv')),
#             expected_checksum
#         )
#
#     def test_create_tmp_files(self):
#         # Test relative path
#         expected_dict = {'assemble_temp_dir': 'test/temp/assemblies',
#                          'fasta_temp_dir': 'test/temp/fastas',
#                          'output_dir': os.path.abspath('output') + '/',
#                          'output_file': os.path.abspath('output/output.csv')}
#         self.assertDictEqual(expected_dict, ectyper.create_tmp_files(
#             'test/temp', output_dir=''))
#         expected_dict = {'assemble_temp_dir': 'test/temp/assemblies',
#                          'fasta_temp_dir': 'test/temp/fastas',
#                          'output_dir': os.path.abspath('output/test'),
#                          'output_file': os.path.abspath('output/test/output.csv')}
#         self.assertDictEqual(expected_dict, ectyper.create_tmp_files(
#             'test/temp', output_dir='test'))
#
#
# if __name__ == '__main__':
#     unittest.main()