class Student:
    def __init__(self,name,house):
            
        self.name = name
        self.house = house
        #self.patronus = patronus


    def __str__(self):
        return f'{self.name} from {self.house}'
    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls (name,house)
        
    @property
    def name (self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError('Missing Name')
        self._name = name



#Getter
    @property
    def house(self):
        return self._house

#Setter
    @house.setter
    def house(self, house):
        if house not in ['Grif', 'Huff', 'Raven', 'Slyth']:
            raise ValueError('Invalid house')
        self._house = house
    

    '''
    def charm(self):
        if self.patronus == 'Stag':
            return '🦌'
        elif self.patronus == 'Otter':
            return '🦦'
        elif self.patronus == 'Jack Russel terrier' or self.patronus == 'Dog':
            return '🐕'
        else:
            return ''

'''

def main():
    info = Student.get()     
    print (info)

    #info.house ='Poop'
    #print(f'{info.name} from {info.house}')
    #print ('Expecto Patronum!')
    #print (info.charm())
    

'''
def get_info():    
    
    name = input('Name: ')
    house = input('House: ')    
    #patronus = input('Patronus: ')
    #return Student(name,house, patronus)
    return Student(name,house)
'''
if __name__ == '__main__':
    main()



'''
############Tuples####################
def main():
    info = get_info()   
    print(f'{info["name"]} from {info["house"]}')

def get_info():    
    info ={}
    info['name'] = input('Name: ')
    info['house'] = input('House: ')
    return info

if __name__ == '__main__':
    main()
'''