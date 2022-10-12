def main():
    #print_col(3)
    #print_row(4)
    print_squ(3)




def print_squ(n):

    for i in range(n): 
        print("# "*n)

main()

def print_col(n):
    for i in range(n): print("#")

def print_row(n):
    print(" ? "*n, sep="")

'''
Nested loops
for i in range(n): 
        for j in range(n):
            print("# ", end="")
        print()
Nested Loops

 for i in range(n): 
        print("# "*n

Nested Loops


x = [
    {"Name":"Bob", "House": "A", "sect":"Baldies"},
    {"Name":"Dob", "House": "A", "sect":"Hairy"},
    {"Name":"Sob", "House": "Z", "sect":"Criers"},
    {"Name":"Lob", "House": "W", "sect":None}
]

for i in x:
    print(i["Name"], i["House"], i["sect"], sep=", ")




x ={"Bob":"A", "Job":"A", "Gob":"C", "Tob":"C"} # dict
for i in x:
    print(i, x[i], sep= " House: ")

x = ["Bob","Harry","Hime"]
for i in range(len(x)): 
    print(x[i])



while True:
    n = int(input("n ? "))
    if n>0:
        break
for i in range(n):
    print("~Nya~")
print("~Nya~\n"*3, end="") #simple loops
for i in range(5):

    print(i,"~Nya~")

i =3
while(i !=0):
    print("~Nya~")
    i-=1

def main():
    x=int(input("x ? "))
    if isEven (x): print ("X is even")
    else : print("x is odd")

def isEven(n):
    #return True if n % 2 ==0 else False
    return (n%2 ==0)

main()
'''