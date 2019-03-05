import httplib
import json
import request

connection =  httplib.HTTPConnection('193.219.91.103:2214')
#body_content = 'BODY CONTENT GOES HERE'
connection.request('GET', "/notes")
result = connection.getresponse()
data1 = result.read()
print data1
print result.status, result.reason
 
 
url = "http://193.219.91.103:2214/notes"
conn =  httplib.HTTPConnection('193.219.91.103:2214')
data = {"title": '#1', "author": 'name', "comment": 'sometext'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
 
#conn.request("POST", "/notes", data = json.dumps(data), headers)
#result = conn.getresponse()
 
result = requests.post(url, data=json.dumps(data), headers=headers)
print result
