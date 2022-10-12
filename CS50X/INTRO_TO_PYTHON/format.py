import re

name = input('Names? ').strip()


if matches := re.search('(^.+), *(.+)$', name): 
    name = matches.group(2) +' '+ matches.group(1)

print(f'hello, {name}')



'''





#################re.matches#########################
import re

name = input('Names? ').strip()


matches = re.search('(^.+), *(.+)$', name)
if matches: 
    name = matches.group(2) +' '+ matches.group(1)

print(f'hello, {name}')




'''