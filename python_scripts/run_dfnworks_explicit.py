"""
.. file:: run_dfnworks.py
   :synopsis: run file for dfnworks 
   :version: 1.0
   :maintainer: Jeffrey Hyman, Carl Gable, Nathaniel Knapp
.. moduleauthor:: Jeffrey Hyman <jhyman@lanl.gov>

"""

import os
import sys
from time import time
sys.path.append("/home/jhyman/dfnworks/dfnworks-main/python_scripts/") 
from modules import dfnworks, helper

def define_paths():
	# Set Environment Variables
	os.environ['PETSC_DIR']='/home/satkarra/src/petsc-git/petsc-3.7-release'
	os.environ['PETSC_ARCH']='/Ubuntu-14.04-nodebug'

	os.environ['PFLOTRAN_DIR']='/home/satkarra/src/pflotran-dev-pt-testing'
	os.environ['DFNWORKS_PATH'] = '/home/jhyman/dfnworks/dfnworks-main/'
	
	os.environ['DFNTRANS_PATH']= os.environ['DFNWORKS_PATH'] +'ParticleTracking/'
	os.environ['DFNGEN_PATH']=os.environ['DFNWORKS_PATH']+'DFNGen/DFNC++Version'
	os.environ['input_files']='/home/jhyman/dfnworks/input_files'

	# Executables	
	os.environ['python_dfn'] = '/n/swdev/packages/Ubuntu-14.04-x86_64/anaconda-python/2.4.1/bin/python'
	os.environ['lagrit_dfn'] = '/n/swdev/mesh_tools/lagrit/install-Ubuntu-14.04-x86_64/3.2.0/release/gcc-4.8.4/bin/lagrit'

	os.environ['connect_test'] = os.environ['DFNWORKS_PATH']+'/DFN_Mesh_Connectivity_Test/ConnectivityTest'
	os.environ['correct_uge_PATH'] = os.environ['DFNWORKS_PATH']+'/C_uge_correct/correct_uge' 


os.system("date")
define_paths()
main_time = time()
DFN = dfnworks.create_dfn()

DFN.make_working_directory()
DFN.check_input()
DFN.create_network()
#DFN.output_report()
DFN.mesh_network()

DFN.lagrit2pflotran()
DFN.pflotran()
DFN.parse_pflotran_vtk()       
DFN.pflotran_cleanup()

DFN.copy_dfnTrans_files()
DFN.run_dfnTrans()

main_elapsed = time() - main_time
timing = 'Time Required: %0.2f Minutes'%(main_elapsed/60.0)
print timing
helper.dump_time(dfn._jobname, dfn._jobname,main_elapsed) 
helper.print_run_time()	
print("*"*80)
print(dfn._jobname+' complete')
print("Thank you for using dfnWorks")
print("*"*80)

