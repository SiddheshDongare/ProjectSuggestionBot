import praw
import re
import json
import random

# connect to reddit
reddit = praw.Reddit('bot1')

# array of subreddits to monitor
subreddits_list = ['learnpython']

# array of replied posts
post_ids = []

# regex to flag target posts
monitor_pattern = r'\b(?:suggest|recommend|give|can you|can someone|what are|can|what|where|beginner|intermediate|advanced|advance|good)(?:\s+\w+)*\s+project('r'?:s)?\b'
monitor_regex = re.compile(monitor_pattern, re.IGNORECASE)

# load comments
with open("comments.json", "r") as comments:
    data = json.load(comments)

# initialize comment objects with random choices from json array
beginner_projects = random.choices([comment for comment in data["beginner_ideas"]], k=5)
intermediate_projects = random.choices([comment for comment in data["intermediate_ideas"]], k=5)
expert_projects = random.choices([comment for comment in data["expert_ideas"]], k=5)
intro_comment = data["introduction"]
closing_comment = data["closing"]

# create empty reply string
reply = ""

# check each subreddit
for subreddit_name in subreddits_list:
    # initialize a subreddit
    subreddit = reddit.subreddit(subreddit_name)
    # check incoming posts while skipping existing posts
    for submission in subreddit.stream.submissions(skip_existing=True):
        # check if post is not already replied too
        # and search for regex pattern in post title
        if (submission.id not in post_ids) and (monitor_regex.search(submission.title)):
            # construct the reply string
            reply += f"{intro_comment}\n"
            reply += f"\nBeginner project ideas:\n"
            for project in beginner_projects:
                project_name = list(project.keys())[0]
                project_url = project[project_name]
                reply += f"{project_name} - [Pseudocode]({project_url})  \n"
            reply += f"\nIntermediate project ideas:\n"
            for project in intermediate_projects:
                project_name = list(project.keys())[0]
                project_url = project[project_name]
                reply += f"{project_name} - [Pseudocode]({project_url})  \n"
            reply += f"\nExpert project ideas:\n"
            for project in expert_projects:
                project_name = list(project.keys())[0]
                project_url = project[project_name]
                reply += f"{project_name} - [Pseudocode]({project_url})  \n"
            reply += f"\n{closing_comment}"
            # reply to the post
            comment = submission.reply(reply)
    # add post id to array
        post_ids.append(submission.id)
