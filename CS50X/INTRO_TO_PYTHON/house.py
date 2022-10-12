name = input('Name? ')

match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Grif')

    case 'Draco':
        print('Slyth')
    case _:
        print('Off to the Sorting Hat')