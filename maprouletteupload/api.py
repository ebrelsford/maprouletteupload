import requests

from .config import API_ROOT


def get_challenge(challenge_id):
    try:
        r = requests.get('%schallenge/%d' % (API_ROOT, challenge_id))
        return r.json()
    except Exception:
        return None


def upload_tasks(api_key, challenge_id, tasks):
    url = '%schallenge/%s/tasks' % (API_ROOT, challenge_id)
    headers = {
        'apiKey': api_key,
    }
    response = requests.post(url, headers=headers, json=tasks)
    return response
