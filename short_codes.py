import instaloader
from instaloader import Post
import time
from time import sleep
from numpy import random

# Read posts list
print('Which is the filename containing the posts codes?')
file = input('path/to/file: ')
f = open(file, 'r+')
posts_codes = f.read().splitlines()
print(len(posts_codes), 'posts to fetch 🦅')

# Get instaloade ready
L = instaloader.Instaloader()
print('Type the folder where to save files:')
folder = input('path/to/folder: ')
L.dirname_pattern = folder

# Login
print('Do you want to login?')
loginFlag = input('Y/n? ')
if loginFlag.lower() == 'y':
    username = input('username: ')
    L.interactive_login(username)

#loop
done = 0
failed = 0
for idx,code in enumerate(posts_codes):
    print('Downloading', code, idx+1, '/', len(posts_codes))
    try:
        post = Post.from_shortcode(L.context, code)
        done += 1
    except:
        print("Something went wrong, item will be skipped.")
        failed += 1
    L.filename_pattern = code
    L.download_post(post, code)    
    sleeptime = random.uniform(1, 3)
    time.sleep(sleeptime)

print('Downloaded posts:', done)
print('Skipped posts:', failed)