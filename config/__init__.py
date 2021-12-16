from typing import Dict

config = {
    'shotgun': {
        'login': '',
        'password': ''
    },
    'telegram_bot': {
        'token': ''
    }
}


def get(name: str) -> Dict[str, str]:
    return config.get(name)
