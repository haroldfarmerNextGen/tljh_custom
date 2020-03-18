import requests

api_url = 'http://localhost:12000/hub/api'
token = '52b462b2d4d34426b7618251ad3fbf49'

data = {'name': 'THISISAGROUP', 'users': ['admin', 'harold']}
r = requests.post(api_url + '/groups/THISISAGROUP/users',
    headers={
             'Authorization': 'token %s' % token,
            },
            json=data
            
    )

r.raise_for_status()
