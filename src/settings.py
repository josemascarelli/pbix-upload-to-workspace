from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Settings:
    CLIENT_ID: str = getenv('CLIENT_ID')
    CLIENT_SECRET: str = getenv('CLIENT_SECRET')
    TENANT_ID: str = getenv('TENANT_ID')
    SEPARATOR: str = getenv('SEPARATOR')
    CHANGED_FILES: str = getenv('CHANGED_FILES')
    WORKFLOW_CONFIG: str = getenv('WORKFLOW_CONFIG')


if __name__ == '__main__':
    print(Settings.CLIENT_ID)
    print(Settings.CLIENT_SECRET)
    print(Settings.TENANT_ID)
    print(Settings.SEPARATOR)
    print(Settings.CHANGED_FILES)
    print(Settings.WORKFLOW_CONFIG)
