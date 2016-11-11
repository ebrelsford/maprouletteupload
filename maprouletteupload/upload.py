import json
import requests


def upload_tasks(api_key, challenge_id, tasks):
    url = 'http://maproulette.org/api/v2/challenge/%s/tasks' % challenge_id
    headers = {
        'apiKey': api_key,
    }
    response = requests.post(url, headers=headers, json=tasks)
    return response
