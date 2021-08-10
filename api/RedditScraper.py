"""
Python Reddit Comment Scraper created by Joshua Stone

Input: URL to subreddit/comment section of subreddit
Output: .txt file with all real comments. Bot comments are filtered out.

Note: change limit in this line: submission.comments.replace_more(limit=50), for
the amount of comments you want.

Limit # for comments returned:
0 = ~500
32 = ~3500
40 = ~4400
50 = ~6000
100 = ~11000
300 = ~23000
600 = ~30000
"""

import praw
from praw.models import MoreComments

class RedditScraper:
    def __init__(self, url, filenameStr):
        self.url = url
        self.filenameStr = filenameStr

    def scrape(self):
        # Create reddit bot instance
        reddit = praw.Reddit(client_id='4Xz6lwJfBY40bw', client_secret='EOU3YORDDveuWyh8Hz8bQbMqJWhc8A', user_agent='WallStreet Scraper')

        # .submission is used for an actual URL, .subreddit is used for a specific subreddit
        submission = reddit.submission(url=self.url)
        print("TESTING: " + self.filenameStr)
        file = open(self.filenameStr, 'a')

        # Loop through comments retreived
        submission.comments.replace_more(limit=2)
        for comment in submission.comments.list():
            # Filters out comments from bots
            if not "bot" in comment.body:
                file.write(comment.body + "\n")

        file.close()
