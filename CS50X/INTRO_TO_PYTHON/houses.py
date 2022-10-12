students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherine"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Mulan", "house": "Ravenclaw"},
    {"name": "Tommy", "house": "Hufflepuff"},
]
houses = set()
for i in students:
    houses.add(i['house'])

print(sorted(houses))
