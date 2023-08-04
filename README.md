
<img src="https://i.ibb.co/Y8RLWzB/pic.pngo" height="300">


# Project Suggestion Bot for Reddit

A Python-based Reddit bot that responds to posts on the r/learnpython subreddit, specifically those seeking project ideas. This bot provides a range of project suggestions that cater to different skill levels, spanning from beginner to advanced in Python programming. 


## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [r/learnpython](https://www.reddit.com/r/learnpython/) - For the project idea itself.



## Demo

[u/ProjectSuggestionBot](https://www.reddit.com/user/ProjectSuggestionBot)


## Features

- The bot promptly provides a curated list of project ideas in response to posts seeking inspiration.

- Keeps a record of replied posts and refrains from responding to them again.

- Exclusively responds to posts created after its initialization.

- Uses regex to identify keywords within post titles, thus reducing false positives.


## Documentation

 - [PRAW API](https://praw.readthedocs.io/en/stable/)


## Environment Variables

To run this project, you will need to edit the praw.ini file and add the following environment variables to it.

`client_id` = "Your bot's client id"   
`client_secret` = "Your bot's's client secret"  
`username` = "Your reddit username"  
`password` = "Your reddit password"  
`user_agent` = "Your bot's user agent"

The `client_id` and `client_secret` can be obtained [here](https://www.reddit.com/prefs/apps).

## Changelog

* v1.0.0
    * Bot replies to posts asking about project ideas with links to suggestions.

## Roadmap

- Clean up code.

- Rewrite with proper OOP's implementation.

- Add functionality to respond to upvotes and downvotes.

- Add more project ideas and references.

- Optimize regex keywords to reduce false positives.

- Utilize OpenAI's and Pastebin's API to generate unique ideas for every new reply. 

