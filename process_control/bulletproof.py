import subprocess
import sys
exit_code = 1

while exit_code != 0:
	exit_code = subprocess.call(['python'] + sys.argv[1:], shell=False)
sys.exit(0)
