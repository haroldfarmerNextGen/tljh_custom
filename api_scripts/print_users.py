import requests

api_url = 'http://localhost:12000/hub/api'
token = '52b462b2d4d34426b7618251ad3fbf49'


r = requests.get(api_url + '/users',
    headers={
             'Authorization': 'token %s' % token,
            }
    )

r.raise_for_status()
users = r.json()
for i in users:
    print(i)