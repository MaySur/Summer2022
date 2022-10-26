import sys

if len(sys.argv)<2: sys.exit("Too few")
#elif len(sys.argv) >30: sys.exit("too many")
for i in sys.argv[1:]:
    print("Hello, bellow", i) 


'''
####sys####
import sys

if len(sys.argv)<2: sys.exit("Too few")
elif len(sys.argv) >2: sys.exit("too many")

print("Hello, bellow", sys.argv[1]) 



####stats####
import statistics
print(statistics.mean([100,90]))

####random  shuffle####
caard = ['jack', 'queen', 'king']

random.shuffle(caard)
for i in caard : print(i)

####random  num####
x=random.randint(1,10)
####random  choice####
x=random.choice(["heads","tails"])

'''
