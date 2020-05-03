# by m81v4n
### INIT
import random as r
import praw

postLimit = 100

print('\nConnecting... ', end='')
reddit = praw.Reddit(client_id="mWwIHYJyhcV97A",  # https://www.reddit.com/prefs/apps
                     client_secret="qamO17spVLJaYFMv6PNltDirse0",
                     password="iskarsoftwareindustries",
                     user_agent="super powers by /u/MrMagicPL",
                     username="iskarsoftware")
print('done\n')

posts = []
subredditsList = ['godtiersuperpowers','shittysuperpowers','titantiersuperpowers','superpowerswithacatch']
for sub in subredditsList:
    print('Fetching posts from '+sub+'... ', end='')
    posts.extend([post for post in reddit.subreddit(sub).hot(limit=postLimit)])
    print('done')
r.shuffle(posts)

print('\neverything ready. we can begin now.')
### LOOP
while True:
    randomPostIndex = r.randint(0, postLimit*4-1)
    randomPost = posts[randomPostIndex]

    print('\n---------------')
    print(randomPost.subreddit)
    print(randomPost.title)
    if randomPost.selftext != '':
        print(randomPost.selftext)

    input()
