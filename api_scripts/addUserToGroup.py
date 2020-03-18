import requests

api_url = 'http://localhost:12000/hub/api'
token = ''

data = {'name': 'THISISAGROUP', 'users': ['admin', 'harold']}
r = requests.post(api_url + '/groups/THISISAGROUP/users',
    headers={
             'Authorization': 'token %s' % token,
            },
            json=data
            
    )

r.raise_for_status()
