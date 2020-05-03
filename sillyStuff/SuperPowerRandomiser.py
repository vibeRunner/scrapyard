# by m81v4n
### INIT
import random as r
import praw

postLimit = 1000

print('\nConnecting... ', end='')
reddit = praw.Reddit(client_id="",  # https://www.reddit.com/prefs/apps
                     client_secret="",
                     password="",
                     user_agent="super powers by /u/MrMagicPL",
                     username="")
print('done\n')

godTier = reddit.subreddit('godtiersuperpowers')
shitty = reddit.subreddit('shittysuperpowers')
titan = reddit.subreddit('titantiersuperpowers')
withCatch = reddit.subreddit('superpowerswithacatch')

# this could be simplified, but there's no urgent need to
print('Fetching posts from GodTierSuperPowers... ', end='')
posts = [post for post in godTier.hot(limit=postLimit)]          # god
print('done')
print('Fetching posts from ShittySuperPowers... ', end='')
posts.extend([post for post in shitty.hot(limit=postLimit)])     # shitty
print('done')
print('Fetching posts from TitanTierSuperPowers... ', end='')
posts.extend([post for post in titan.hot(limit=postLimit)])      # titan
print('done')
print('Fetching posts from SuperPowersWithACatch... ', end='')
posts.extend([post for post in withCatch.hot(limit=postLimit)])  # withCatch
print('done')
r.shuffle(posts)

print('\neverything ready. we can begin now.')
### LOOP
while True:
    randomPostIndex = r.randint(0, postLimit-1)
    randomPost = posts[randomPostIndex]

    print('\n---------------')
    print(randomPost.subreddit)
    print(randomPost.title)
    if randomPost.selftext != '':
        print(randomPost.selftext)

    input()
