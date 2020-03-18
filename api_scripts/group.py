import requests

api_url = 'http://localhost:12000/hub/api'
token = ''


r = requests.get(api_url + '/groups',
    headers={
             'Authorization': 'token %s' % token,
            }
    )

r.raise_for_status()
groups = r.json()
for i in groups:
    print(i)
