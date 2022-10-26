import argparse

pars = argparse.ArgumentParser(description  ='Nyas like a cat')
pars.add_argument('-n', default =1 ,help = 'numenr of times to meow', type =int)
args = pars.parse_args()

for i in range(args.n):
    print('~NYA~')