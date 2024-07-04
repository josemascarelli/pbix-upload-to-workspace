from urllib import parse

import requests


def deploy_pbix(
    workspace_id: str,
    report_name: str,
    access_token: str,
    file_binary: bytes,
):
    print(f'Uploading {report_name} to workspace {workspace_id}...')
    url = (
        f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/imports?'
        f'datasetDisplayName={parse.quote(report_name)}&'
        f'nameConflict=CreateOrOverwrite'
    )

    response = requests.post(
        url=url,
        headers={
            'Authorization': f'Bearer {access_token}',
        },
        files={
            'file': file_binary,
        },
    )

    if response.status_code not in [200, 201, 202, 204]:
        raise Exception(
            {
                'error': {
                    'status_code': response.status_code,
                    'message': response.content,
                    'url': response.url,
                }
            }
        )
