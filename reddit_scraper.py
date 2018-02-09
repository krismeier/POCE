import praw #Reddit parsing library

#Reddit API ID and Secret setup
reddit = praw.Reddit(client_id='MyID', client_secret='MySecret', user_agent='MyAgent')

#Good and CLEAN test subreddits: -learnpython

#Loop through all new posts in defined subreddits looking for defined keywords and print out matches.
#Match in submission title, body text, and associated URL
keyword_list = ['test1', 'test2']
for submission in reddit.subreddit('all').stream.submissions():
    for keyword_item in keyword_list:
        if keyword_item in submission.title or keyword_item in submission.selftext or keyword_item in submission.url:
            print("----------------------------")
            prestr = submission.title + "::" + submission.selftext + "::" + submission.url
            print prestr.encode('utf-8')
