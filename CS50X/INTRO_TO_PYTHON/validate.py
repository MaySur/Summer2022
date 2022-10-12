import re
# [a-zA-Z0=9_] same as \w
email = input('Email?: ').strip()
if re.search('^(\w|\.)+@(\w+\.)?\w+\.edu$',email,re.IGNORECASE):
    print('Valid')
else: 
    print('Invalid')

