import csv
students = []
with open('names.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'name': row['name'], 'home': row['country']})

def get_name(student):
    return student['name']
for i in sorted(students, key = get_name): 
    print(f'{i["name"]} is in {i["home"]}')




'''
################### CSV ###################
import csv
students = []
with open('names.csv') as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({'name': name, 'home': home})

def get_name(student):
    return student['name']
for i in sorted(students, key = get_name): 
    print(f'{i["name"]} is in {i["home"]}')
### DIctreader############
import csv
students = []
with open('names.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'name': row['name'], 'home': row['country']})

def get_name(student):
    return student['name']
for i in sorted(students, key = get_name): 
    print(f'{i["name"]} is in {i["home"]}')




###############Read File#################
with open ('names.txt', 'r') as file:
    for i in file:
        print('Hey', i.rstrip())

names = []

with open('names.txt') as file:
    for i in file:
        names.append(i.rstrip())
for i in sorted (names):
    print('hey', i)




with open('names.csv') as file:
    for i in file:
       a,b = i.rstrip().split(',')
       print(f'{a} is in {b}')



    students = []

with open('names.csv') as file:
    for i in file:
        a,b = i.rstrip().split(',')
        student= {'name': a, 'house': b}
        students.append(student)
def get_name(student):
    return student['name']
for i in sorted(students, key = get_name): 
    print(f'{i["name"]} is in {i["house"]}')

  ############ Write File#################
  name = input('Name?? ')

with open('names.txt', 'a') as file:
    file.write(f'{name} \n')

  
  '''