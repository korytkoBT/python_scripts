#!/usr/bin/env python 

import sys
import signal
import os
import datetime
import time
import crashingCommon


FILE_NAME = 'lockfile'

pidfile = crashingCommon.get_pidfile(sys.argv)

def cleanup(signum, frame):
    os.remove(pidfile)
    if signum == signal.SIGTERM:
        sys.exit(0)
    else:
        sys.exit(1)


if os.path.isfile(pidfile):
    sys.stderr.write("Cannot continue pidfile for instance already exists")
    sys.exit(1)
else:
    with open(pidfile, 'w+') as f:
	f.write(str(os.getpid()))

signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGUSR1, cleanup)

while os.path.isfile(FILE_NAME):
    sys.stdout.write(format(datetime.datetime.now()) + " Hello changed yes!\n")
    sys.stdout.flush()
    time.sleep(1)

cleanup(None, None)

sys.stderr.write("No lockfile")
sys.stderr.flush()
sys.exit(1)

