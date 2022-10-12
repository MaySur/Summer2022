import re

url = input('URL: ').strip()

#usern = url.removeprefix('https://twitter.com/')

if matches:=re.search('^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)', url, re.IGNORECASE):
    print(f'Username:', matches.group(1))








'''
######################## re.sub############

import re

url = input('URL: ').strip()

#usern = url.removeprefix('https://twitter.com/')

usern =re.sub('^(https?://)?(www\.)?twitter\.com/','',url)
print('Username:',user

'''