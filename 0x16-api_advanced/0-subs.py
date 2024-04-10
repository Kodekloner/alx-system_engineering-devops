#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    headers = {'User-Agent': 'web application:intranet.alxswe.com:v1.0 (by /u/Bale237)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.HTTPError as http_err:
        return 0
    except requests.exceptions.RequestException as e:
        return 0
    except ValueError as json_err:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
