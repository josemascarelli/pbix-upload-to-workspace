import requests


def get_access_token(client_id: str, client_secret: str, tenant_id: str):
    response = requests.get(
        f'https://login.microsoftonline.com/{tenant_id}/oauth2/token',
        data={
            'client_id': client_id,
            'grant_type': 'client_credentials',
            'resource': 'https://analysis.windows.net/powerbi/api',
            'response_mode': 'query',
            'client_secret': client_secret,
        },
    )
    access_token = response.json()['access_token']

    return access_token
