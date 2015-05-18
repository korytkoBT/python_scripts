import re
import sys

localips = ["127.0.0.1", "10.0.2.15"]

loglinep = r'(?P<ip>\d*\.\d*\.\d*\.\d*)[^\[]*[^\]]*] "(\S*) (?P<path>\S*) (\S*)" (?P<status>\d*)'
with open(sys.argv[1], "r") as logfile:
    error_path = []
    remote_calls = not_found_errors = 0
    for line in logfile:
        match = re.match(loglinep, line)
        ip =  match.groupdict()['ip']
        path = match.groupdict()['path']
        status = match.groupdict()['status']
        
        if ip not in localips:
            remote_calls += 1
	    if status == '404':
                not_found_errors += 1
                error_path.append(path)

print "%2.2f of all calls were 404" % (float(not_found_errors)/remote_calls,)
print "list of all paths that were not found"
for p in error_path:
    print p
        

#127.0.0.1 - - [16/May/2015:11:49:46 +0200] "GET / HTTP/1.1" 200 3594 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"
