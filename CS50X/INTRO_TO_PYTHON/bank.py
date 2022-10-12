class Account:
    def __init__(self):
        self._bal =0
    
    @property
    def bal(self):
        return self._bal
    def depo(self, n):
        self._bal +=n

    def withdr(self,n):
        self._bal -= n

def main():
    acc = Account()
    print ('Balance:', acc.bal)
    acc.depo(150)
    acc.withdr(245)
    print('Balance:', acc.bal)
    
if __name__ =='__main__':
    main()

















"""
bal = 0

def main():
    print ('Balance:', bal)
    depo(150)
    withdr(245)
    print('Balance:', bal)

def depo (n):
    global bal
    bal += n


def withdr(n):
    global bal
    bal -= n

if __name__ =='__main__':
    main()
"""