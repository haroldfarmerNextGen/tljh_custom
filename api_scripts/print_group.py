import requests

api_url = 'http://localhost:12000/hub/api' #Juyterhub URL
token = '5921bc46c0e24400b8e35882a239f725' #Token can be created in the control panel of Jupyterhub


r = requests.get(api_url + '/groups',
    headers={
             'Authorization': 'token %s' % token,
            }
    )

r.raise_for_status()
groups = r.json()
for i in groups:
    print(i)