"""
import csv

name = input('Name? ')
home = input('Where u from? ')

with open ('apple.csv','a') as file:
    writer = csv.DictWriter({file}, fieldnames = ['name', 'home'])
    writer.writerow({'name': name, 'home': home})

"""
