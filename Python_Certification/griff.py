students = ['Hermione', 'Harry', 'Ron']
for i, student in enumerate(students):
    print(i+1, student)
















"""students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherine"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Mulan", "house": "Ravenclaw"},
    {"name": "Tommy", "house": "Hufflepuff"},
]

griff = [
    i['name'] for i in students if i['house'] == 'Gryffindor'
    ]

for i in sorted(griff):
    print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherine"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Mulan", "house": "Ravenclaw"},
    {"name": "Tommy", "house": "Hufflepuff"},
]


def is_griff(s):
    return s["house"] == "Gryffindor"


griff = filter(is_griff, students)


for i in sorted(griff, key=lambda s: s["name"]):
    print(i["name"])

  
  
  
  
  
  students = ['Hermione', 'Harry', 'Ron']


griff ={student: 'Gryffindor' for student in students}

#griff =[{'name': student, 'house': 'Gryffindor'} for student in students]

print(griff)
  
  
  
    """
