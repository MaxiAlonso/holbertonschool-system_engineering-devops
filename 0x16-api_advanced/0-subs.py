#!/usr/bin/python3
"""
Task 0 - 0x16. API advanced
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Get a copy of the default headers that requests would use
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
    response = requests.get(url, headers=headers).json()
    suscribers = response.get('data').get('subscribers')
    if suscribers is None:
        return (0)
    return (suscribers)
