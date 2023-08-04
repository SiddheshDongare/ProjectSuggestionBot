import praw
import re

reddit = praw.Reddit('bot1')
subreddits_list = ['learnpython']
post_ids = []

monitor_pattern = r'\b(?:suggest|recommend|give|can you|can someone|what are|can|what|where|beginner|intermediate|advanced|advance|good)(?:\s+\w+)*\s+project('r'?:s)?\b'
monitor_regex = re.compile(monitor_pattern, re.IGNORECASE)

for subreddit_name in subreddits_list:
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.stream.submissions(skip_existing=True):
        if (submission.id not in post_ids) and (monitor_regex.search(submission.title)):
            comment = submission.reply("""Beepbop, I'm a bot. Here are some interesting sources for project ideas which you can implement:  
  
[1. GeeksForGeeks: Python Projects Beginner to Advanced](https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/)  
[2. freeCodeCamp: 25 Python Projects for Beginners](https://www.freecodecamp.org/news/python-projects-for-beginners/)  
[3. The-Cool-Coder](https://github.com/The-Cool-Coders/Project-Ideas-And-Resources)  
[4. Parvat Computer Technology Playlist](https://www.youtube.com/watch?v=6CZB6VTy3Hg&list=PLl316cKxhMxtOWHa88kDqm42uWz1aqGfD)  
[5. Real Python's Intermediate Project List](https://realpython.com/intermediate-python-project-ideas/)  


Or better yet, create a python Reddit bot using the [PRAW](https://praw.readthedocs.io/en/stable/) library to respond to reddit posts asking for project suggestions.""")

    post_ids.append(submission.id)
