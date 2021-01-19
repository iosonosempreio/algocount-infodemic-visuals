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
done = []
failed = []
for idx,code in enumerate(posts_codes):
    print('Downloading', code, idx+1, '/', len(posts_codes))
    try:
        post = Post.from_shortcode(L.context, code)
        done.append(code)
    except:
        print("Something went wrong, item will be skipped.")
        failed.append(code)
    L.filename_pattern = code
    L.download_post(post, code)    
    sleeptime = random.uniform(1, 3)
    time.sleep(sleeptime)

print('Downloaded posts:', len(done))
print('Skipped posts:', len(failed))

with open(folder + "/failed.csv", "w") as txt_file:
    txt_file.write("not_downlaoded\n")
    for code in failed:
        txt_file.write(code + "\n")