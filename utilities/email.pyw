# Send a HTTP POST request to our outside server so I can reliably
# send an email.
#
# arg1: The name of the FC that croaked

import urllib, urllib2, sys

# set up HTTP POST request
url = 'http://yourserver/sendemail.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'email' : '',
          'url' : '',
          'agent' : '',
          'subject' : 'ETL Job Exploded: ' + sys.argv[1],
          'to' : 'you@email.com',
          'message' : 'Oh dear. The ' + sys.argv[1] +' went boom. Might want to check that out.' }
headers = { 'User-Agent' : user_agent }

# send HTTP POST request
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
urllib2.urlopen(req)
