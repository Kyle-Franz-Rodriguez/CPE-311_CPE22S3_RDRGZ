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

def showtotal(nocross, land1, land2):
    print("--------------------\nHaven't crossed':\n",
          [i.name for i in land1],[i.name for i in nocross], '\n')
    print("Crossed:\n",
          [i.name for i in land2], "\n--------------------\n")

def cross_river(land1, boat = [], land2 = [], counter = 0, capacity = 100):
    for i in land1:
        print([i.name, i.weight])
    print("...wants to cross in a boat with a capacity of", capacity, '\n')
    # Check for people who exceeds capacity
    notcrossed = []
    for i in land1[:]:
        if i.weight > capacity:
            print(i.name, "exeeded the weight limit, can not cross!")
            notcrossed.append(land1.pop(land1.index(i)))
    # Show people in land1 and land2
    showtotal(notcrossed, land1, land2)
    # Check for head count. This will be used as a stopping point
    # so that no one comes back by the end of the loop
    heads = len(land1)
    # The loop
    while land1:       
        # Sort group in ascending order
        land1.sort(key = lambda x : x.weight)
        # 1 person should be in the boat
        for i in land1[:]:
            if i.sentient == True:
                if i.weight <= capacity:
                    boat.append(i)
                    counter += i.weight
                    land1.remove(i)
                    break
        # Stop if everything in land1 is an item
        if boat == []:
            print("All loads are items! Items can not cross by themselves!\n")
            break
        # To find people or items to go with the person
        for i in land1[:]:
            if counter + i.weight <= capacity:
                boat.append(i)
                counter += i.weight
                land1.remove(i)
        # When the objects left in land1 are more than 100 when added
        # to remove infinite loop
        if len(boat) == 1:
            # The object on the boat exchange places with the first index in land1
            land1.append(boat.pop())
            boat.append(land1[0])
            del land1[0]
            if (boat[0]).sentient == False:
                # The boat contains an item that can't cross by itself
                print((boat[0]).name, "can't cross alone!\n")
                notcrossed.append(boat.pop(0))
                heads -= 1
                continue
        # Show all people that are crossing
        print([i.name for i in boat], "is crossing in a boat\n")
        # Send boat load to land2
        for i in boat: land2.append(i)
        boat.clear()
        # Print land2
        print([i.name for i in land2], "reached the other side!\n")
        # If only 1 person can cross
        if len(land2) == 1 and len(land1) >= len(land2):
            print("Only 1 person is able to cross...\n")
            showtotal(notcrossed, land1, land2)
            break
        # Check if done, so that no one comes back as the loop ends.
        if len(land2) == heads:
            #Just add notcrossed to land1
            for i in notcrossed:
                land1.append(i)
            showtotal(notcrossed, land1, land2)
            print("!!!---All are able to cross---!!!\n")
            #check for people who are not able to cross
            if notcrossed:
                print("Except for", [i.name for i in notcrossed],"...sadly.\n")
            break
        # Reset counter
        counter = 0
        # 1 person of least weight should go back
        land2.sort(key = lambda x : x.weight)
        for i in land2[:]:
            if i.sentient == True:
                land1.append(i)
                land2.remove(i)
                print([i.name], "went back\n")
                break
    return land2
#---------------------------------------------------------------------------
Roman = Person("Roman", 90)
Verlyn = Person("Verlyn", 80)
Lloyd = Person("Lloyd", 60)
Robin = Person("Robin", 40)
Supplies = Item("Supplies", 20)
crosser = [Roman, Verlyn, Lloyd, Robin, Supplies]
print("Successful crosser:\n", [i.name for i in cross_river(crosser)])