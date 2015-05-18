from optparse import OptionParser
import os
import ConfigParser

def get_pidfile(args):
	parser = OptionParser()
	parser.add_option("-i", "--instance", dest="instance",
			  help="specify instance number", metavar="INSTANCE")

	options, args = parser.parse_args(args)

	confParser = ConfigParser.SafeConfigParser()
	confParser.read(['crashing.cfg', os.path.expanduser('~/.crashing.cfg')])

	rundir = confParser.get('runtime', 'rundir')

	pidfile = os.path.join(rundir, "crashing.%s.pid" % (options.instance,))
        return pidfile
