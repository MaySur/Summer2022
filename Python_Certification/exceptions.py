def main():
    x = get_int("x? ")
    print ("x is", x)

def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            pass
    
main()       















'''
######################### modified  Try################


def main():
    x = get_int()
    print ("x is", x)

def get_int():
    while True:
        try: 
            return int(input("x? "))
        except ValueError:
            pass
    
main()       


######################### Whilw with Try################
while True:

    try: 
        x = int(input("x? "))
        break
    except ValueError:
        print ("Not int")
    
        

print(f"x is {x}"
############################Intial Try Function #########
try: 
    x = int(input("x? "))
    
except ValueError:
    print ("Not int")
else:
    print (f"x is {x}")




'''