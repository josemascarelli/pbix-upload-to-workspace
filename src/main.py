from services import deploy_pbix, get_access_token
from settings import Settings
from utils import get_files, get_workspace_id

settings = Settings()


def main():
    access_token = get_access_token(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        tenant_id=settings.TENANT_ID,
    )

    files = get_files(
        files=settings.CHANGED_FILES, separator=settings.SEPARATOR
    )

    for file in files:
        if file['file_binary'] is None:
            continue

        workspace_id = get_workspace_id(
            workspace_name=file['file_workspace'],
            workflow_config=settings.WORKFLOW_CONFIG,
        )
        deploy_pbix(
            workspace_id=workspace_id,
            report_name=file['file_name'],
            access_token=access_token,
            file_binary=file['file_binary'],
        )


if __name__ == '__main__':
    main()
