import requests

api_url = 'http://localhost:12000/hub/api'
token = '5921bc46c0e24400b8e35882a239f725'


r = requests.delete(api_url + '/groups/THISISATESTGROUP',
    headers={
             'Authorization': 'token %s' % token,
            }
    )

r.raise_for_status()

