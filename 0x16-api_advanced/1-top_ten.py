#!/usr/bin/python3
"""
get the number_of_subscribers function
"""

import requests

def top_ten(subreddit):
    """Return the top 10 hottes posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit":10
    }
    response = requests.get(url, headers=headers,params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return 0
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
