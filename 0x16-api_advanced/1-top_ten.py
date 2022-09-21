#!/usr/bin/python3
"""
Task 1 - 0x16. API advanced
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    # Get a copy of the default headers that requests would use
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
