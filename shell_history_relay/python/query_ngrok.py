import requests


r = requests.get("http://localhost:4040/api/tunnels")
decoded = r.json()

for tunnel in decoded['tunnels']:
    for x, y in tunnel.items():
        print(x,y)
    print()


    
