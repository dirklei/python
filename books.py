__author__ = 'yulei'

#Filename:MyAddressBook.py
import cPickle as p
import os
#Class Item
class Item:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
#the main menu of address book
def menu():
    '''the main menu of address book'''
    print ''
    print '1.Insert an item'
    print '2.Delete an item'
    print '3.Modify an item'
    print '4.Display all items'
    print '5.Sort all items'
    print '6.Exit the program'
    print 'What do you want to do?'

#initialization of system, load the member list
def begin():
    '''initialization of system, load the member list'''
    global itemlist
    if os.path.exists('memberlist.data') == True:#to judge whether the file exists
        listfile = file('memberlist.data','r')
        if len(listfile.read())!=0:#to judge whether the file is empty
            itemlist = p.load(listfile)
        listfile.close()
#exitance of system, store the menber list
def end():
    '''exitance of system, store the menber list'''
    global itemlist
    listfile = file('memberlist.data','w+')
    p.dump(itemlist,listfile)
    listfile.close()
#insert an item into the member list
def insert():
    '''insert an item into the member list'''
    name = raw_input('Enter name:')
    age = int(raw_input('Enter age:'))
    gender = raw_input('Enter gender:')
    item = Item(name,age,gender)
    global itemlist
    itemlist.append(item)
#print an item
def output(item):
    '''print an item'''
    print '%-15s%-5d%s'%(item.name,item.age,item.gender)
#print all items
def display():
    '''print all items'''
    global itemlist
    l = len(itemlist)
    print 'name           age  gender'
    for i in range(0,l):
        output(itemlist[i])
    print ''
#delete an item by name from member list
def delete():
    '''delete an item by name from member list'''
    name = raw_input('Enter the name you want to delete:')
    global itemlist
    l = len(itemlist)
    for i in range(0,l):
        if (itemlist[i].name == name):
            itemlist.pop(i)
#update an item
def update(item):
    '''update an item'''
    item.name = raw_input('Enter name:')
    item.age = int(raw_input('Enter age:'))
    item.gender = raw_input('Enter gender:')
#update an item's information by name
def modify():
    '''update an item's information by name'''
    name = raw_input('Enter the name you want to modify:')
    global itemlist
    l = len(itemlist)
    for i in range(0,l):
        if (itemlist[i].name == name):
            update(itemlist[i])
    print 'Update done!'
#sort all items by name
def sort():
    global itemlist
    itemlist.sort(None,key = lambda item:item.name)
#Here are the scripts
itemlist = [] #Notice here!!!
begin()
while True:
    menu()
    sel = int(raw_input())
    if sel == 1:
        insert()
    elif sel == 2:
        delete()
    elif sel == 3:
        modify()
    elif sel == 4:
        display()
    elif sel == 5:
        sort()
    else:
        break
end()
print 'Good Bye!'
