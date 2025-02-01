# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:33:25 2025
@Created by: Liv, Kyle
"""
class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.sentient = False

class Person(Item):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sentient = True

def cross_river(land1, boat = [], land2 = [], counter = 0, capacity = 100):

    for i in land1:
        print([i.name, i.weight])
    print("...wants to cross in a boat with a capacity of", capacity)
    print()
    
    #Check for people who exceeds capacity
    for i in land1:
        if i.weight > capacity:
            print(i.name, "can not cross")
            land1.remove(i)
    print()
    
    #Show people in land1
    print("--------------------")
    print("Current people in land 1")
    for i in land1:
        print([i.name, i.weight])
    print()
    
    #Show people in land2
    print("Current people in land 2")
    for i in land2:
        print([i.name, i.weight])
    print("--------------------")
    print()
    
    #Check for head count
    heads = len(land1)
    
    #The loop
    while land1 != []:
        for i in land1:
            #Sort group in ascending order
            land1.sort(key = lambda x : x.weight)
            
            #1 person should be in the boat
            for i in land1:
                if i.sentient == True:
                    if i.weight <= capacity:
                        boat.append(i)
                        counter += i.weight
                        land1.remove(i)
                        break
                    else: continue
            
            #To find people to go with the person
            for i in land1:
                if counter + i.weight <= capacity:
                    counter += i.weight
                    boat.append(i)
                    land1.remove(i)
            if len(boat) == 1:
                remove = boat.pop()
                boat.append(land1[0])
                del land1[0]
                land1.append(remove)
            
            #print initial boat
            for i in boat:
                print([i.name, i.weight])
            print("is crossing in a boat")
            print()
            
            #Send boat load to land2
            for i in boat:
                land2.append(i)
            boat.clear()
            
            #Print land2
            for i in land2:
                print([i.name, i.weight])
            print("...crossed")
            print()
            
            #Check if done
            if len(land2) == heads:
                #Show people in land1
                print("--------------------------------------------------------------")
                print("Current people in land 1")
                for i in land1:
                    print([i.name, i.weight])
                print()
                
                #Show people in land2
                print("Current people in land 2")
                for i in land2:
                    print([i.name, i.weight])
                print("--------------------------------------------------------------")
                print()
                break
            
            #Reset
            counter = 0
            
            #1 person of least weight should go back
            land2.sort(key = lambda x : x.weight)
            for i in land2:
                if i.sentient == True:
                    land1.append(i)
                    land2.remove(i)
                    print([i.name], "went back")
                    print()
                    break
            
            #Show people in land1
            print("--------------------------------------------------------------")
            print("Current people in land 1")
            for i in land1:
                print([i.name, i.weight])
            print()
            
            #Show people in land2
            print("Current people in land 2")
            for i in land2:
                print([i.name, i.weight])
            print("--------------------------------------------------------------")
            print()

#-----------------------------------------------------------------------------

Roman = Person("Roman", 90)
Victor = Person("Victor", 120)
Verlyn = Person("Verlyn", 80)
Lloyd = Person("Lloyd", 60)
Robin = Person("Robin", 40)
Supplies = Item("Supplies", 20)
crosser = [Roman, Verlyn, Lloyd, Robin, Supplies]

cross_river(crosser)
