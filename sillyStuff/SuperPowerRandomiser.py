# by m81v4n
### INIT
import random as r
import praw

postLimit = 100

print('\nConnecting... ', end='')
reddit = praw.Reddit(client_id="",  # https://www.reddit.com/prefs/apps
                     client_secret="",
                     password="",
                     user_agent="super powers by m81v4n",
                     username="")
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
    randomPostIndex = r.randint(0, len(posts)-1)
    randomPost = posts[randomPostIndex]

    print('\n---------------')
    print(randomPost.subreddit)
    print(randomPost.title)
    if randomPost.selftext != '':
        print(randomPost.selftext)

    posts.pop(posts.index(randomPost))
    input()
