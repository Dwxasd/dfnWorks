# automatically changes path names in tests directory and pydfnworks

import subprocess
import sys, os

def replace(old, new):
    subprocess.call("find ../ -type f -print0 | xargs -0 sed -i -e 's@" + old + "@" + new + "@g'", shell=True)
    subprocess.call("find ../../tests -type f -print0 | xargs -0 sed -i -e 's@" + old + "@" + new + "@g'", shell=True)

old = 'DUMMY'
new = os.getcwd().split('/dfnWorks')[0]
print 'replacing ', old, ' with ', new 
replace(old, new)
