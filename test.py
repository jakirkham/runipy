
import unittest
from glob import glob
from os import path, chdir

from IPython.nbformat.current import read

from runipy.notebook_runner import NotebookRunner
from runipy.testbase import TestRunipyBase

class TestRunipy(TestRunipyBase):

    def testRunNotebooks(self):
        notebook_dir = path.join('tests', 'input')
        for notebook_path in glob(path.join(notebook_dir, '*.ipynb')):
            notebook_file = path.basename(notebook_path)
            print notebook_file
            expected_file = path.join('tests', 'expected', notebook_file)
            runner = NotebookRunner(read(open(notebook_path), 'json'), working_dir=notebook_dir)
            runner.run_notebook(True)
            expected = read(open(expected_file), 'json')
            self.assert_notebooks_equal(expected, runner.nb)


if __name__ == '__main__':
    unittest.main()

