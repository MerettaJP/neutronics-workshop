
""" test_script.py: run all the examples in the openmc workshop and check each example produces the expected results.
    The example scripts open up various plots, some of which pause / block the running of this test suite.
    The running of the tests can be manually resumed by closing matplotlib and eog windows when they pop up
    run with
    pytest test_scripts.py
"""

# at the moment, we are only testing to see whether the outputs are created
# we are NOT testing to see whether the outputs are also saved locally
# this will have to be implemented

from pathlib import Path 
import os
import pytest
import unittest

cwd = os.getcwd()





class test_task_9(unittest.TestCase):
    def test_task_9_part_1(self):
        # assumes get_true_values_1d.py has been run previously and json file in repo
        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_9'))
        output_filenames = ['simulation_results.json', 'output.gif']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python 1_lithium_enrichment_optimisation.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() is True
            os.system('rm '+output_filename)

    def test_task_9_part_2(self):
        # lithium_enrichment_and_thickness_optimisation.py
        # test output (output not actually working yet)
        # 2_lithium_enrichment_and_thickness_optimisation.py
        pass
