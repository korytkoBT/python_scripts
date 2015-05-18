import crashingCommon
import sys
import os
import signal

pidfile = crashingCommon.get_pidfile(sys.argv)
with open(pidfile, 'r') as f:
    pid = int(f.readline().strip())
    os.kill(pid, signal.SIGTERM)

sys.exit(0) 
