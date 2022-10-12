def main():
    yell('Life' , 'is', 'a', 'drag')


def yell(*words):
    uppercased = [i.upper() for i in words]
    print(*uppercased)
main()


"""def f (*objcts, **kwargs):
    print('Named : ', objcts)

f(100,50,25)


def main():
    yell('Life' , 'is', 'a', 'drag')


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
main()












def total(galleons, sickles, knuts):
    return(galleons *17 + sickles) * 29 + knuts
coins = [100,50,25]
print (total(*coins), 'Knuts')
"""