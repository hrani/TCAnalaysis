""" setup.py : Script for FindSim """
__author__      = "HarshaRani"
__copyright__   = "Copyright 2021 HillTau, NCBS"
__maintainer__  = "HarshaRani"
__email__       = "hrani@ncbs.res.in"

import os,sys,subprocess
import sys
#sys.path.append(os.path.dirname(__file__))
import setuptools
#from distutils.core import setup, Extension
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class git_clone_external(build_ext):
    def run(self):
        print("[INFO ] Running tests... ")
        #subprocess.check_call([os.path.isdir(extern/pybind11)]) 
        #subprocess.check_call(['git', 'clone', 'https://github.com/pybind/pybind11/','extern/pybind11/'])
        build_ext.run(self)

class get_pybind_include(object):
	def __init__(self,user=False):
		self.user = user
	def __str__(self):
		import pybind11
		print(pybind11.get_include(self.user))
		return pybind11.get_include(self.user)
		
setuptools.setup(
        name="TCAnalysis",
        description="The code base is to use of timeCell python module on Matlab files",
        version="1.0",
        author= "Upinder S. Bhalla",
        author_email="bhalla@ncbs.res.in",
        maintainer= "HarshaRani",
        maintainer_email= "hrani@ncbs.res.in",
        long_description = open('README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        cmdclass = {'build_ext': git_clone_external},
        packages=["TimeCellAnalysis","TimeCellAnalysis.TcPy"],
        package_dir={'TimeCellAnalysis': "."},
        ext_modules=[Extension('tca', ['TcPy/tcDefaults.cpp','TcPy/tiScore.cpp'], include_dirs=['extern/pybind11/include'])],
        install_requires = ['numpy','matplotlib','h5py'],
	url ="http://github.com/bhallalab/timecellanalysis",
	package_data = {"TimeCellAnalysis" : ['TcPy/*.py']},
	license="GPLv3",
	entry_points = {
	
		'console_scripts' : [ 'TimeCellDemo = TimeCellAnalysis.__main__:run',
				      'TimeCellBenchmark = TimeCellAnalysis.__main__:run_benchmark',
				      'TimeCellGroundtruth = TimeCellAnalysis.__main__:run_ground_truth',
				      'TimeCellR2b = TimeCellAnalysis.__main__:run_r2bdemo',
				      'TimeCellBatchanalysis = TimeCellAnalysis.__main__:run_batchanalysis'
				   ]
			},
		)


'''
""" setup.py : Script for FindSim """
__author__      = "HarshaRani"
__copyright__   = "Copyright 2021 HillTau, NCBS"
__maintainer__  = "HarshaRani"
__email__       = "hrani@ncbs.res.in"

import os
import sys
sys.path.append(os.path.dirname(__file__))
import setuptools
#from distutils.core import setup, Extension
from setuptools import setup, Extension
setuptools.setup(
        name="TCAnalysis",
        description=" ",
        version="1.0",
        author= "Upinder S. Bhalla",
        author_email="bhalla@ncbs.res.in",
        maintainer= "HarshaRani",
        maintainer_email= "hrani@ncbs.res.in",
        long_description = open('README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        packages=["TimeCellAnalysis","TimeCellAnalysis.TcPy"],
        package_dir={'TCAnalysis': "."},
        ext_modules=[Extension('tc', ['TcPy/tcDefaults.cpp'], include_dirs=['extern/pybind11/include'])],
        install_requires = ['numpy','matplotlib','h5py'],
        
        #dependency_links=[
        # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
        #'git+ssh://git@github.com/pybind/pybind11.git#egg=ExampleRepo-0.1'],
	url ="http://github.com/bhallalab/TimeCellAnalysis",
	package_data = {"TCAnalysis" : ['TcPy/timeCellMatlabExample.py']},
	license="GPLv3",
	entry_points = {
	
		'console_scripts' : [ 'TCAnalysis = TCAnalysis.__main__:run'
				   ]
			},
		)
'''
