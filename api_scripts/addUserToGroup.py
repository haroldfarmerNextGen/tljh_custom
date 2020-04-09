import requests

api_url = 'http://localhost:12000/hub/api'
token = '5921bc46c0e24400b8e35882a239f725'

data = {'name': 'dev', 'users': ['jimmy','john']}
r = requests.post(api_url + '/groups/dev/users',
    headers={
             'Authorization': 'token %s' % token,
            },
            json=data
            
    )

r.raise_for_status()
