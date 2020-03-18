import requests

api_url = 'http://localhost:12000/hub/api'
token = ''


r = requests.get(api_url + '/users',
    headers={
             'Authorization': 'token %s' % token,
            }
    )

r.raise_for_status()
users = r.json()
for i in users:
    print(i)
