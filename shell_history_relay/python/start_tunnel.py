import requests
from requests.exceptions import ConnectionError
import json 

# is ngrok running
try:
	r = requests.get('http://localhost:4040/api')
except ConnectionError:
	print('ngrok not running\n run the command\n$ ~/ngrok start --none')
	exit(1)
print(r.json())



data = {"name":"swc","addr":"file:///Users/jteitelbaum","proto":"http"}
payload = json.dumps(data)

r = requests.post('http://localhost:4040/api/tunnels', json=data)
print(r.json())
