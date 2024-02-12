

class Person:
    def __init__(self, name, location):
        self.name = name
        self.health = 100
        self.armor = 0
        self.inventory = []
        self.equipped_item = None
        self.location = 
    
    def equip_item(self, selection):
        selection.lower()
        if selection in self.inventory:
            self.equipped_item = self.inventory[self.inventory.index(selection)]
        else:
            print('Item not found in inventory, did you mistype?')
    
    def attack(self):
        pass

    def grab_item(self, selection, room):
        if type(room.selection) == type(Item):
            self.inventory.append(selection)

    def search_area(self):
        pass

    def die(self):
        pass

class Room:
    def __init__(self, furniture = None, items = None, connected_doors = None):
        if furniture is None:
            furniture = []
        
        if items is None:
            items = []
        
        if connected_doors is None:
            connected_doors = {}

        self.furniture = furniture
        self.items = items
        self.connected_doors = connected_doors

class Item:
    def __init__(self, name, hitpoints=0, defpoints=0, healfactor=0, consumable = True, num_uses = 1): 
        self.name = name
        self.damage = hitpoints
        self.defense = defpoints
        self.healfactor = healfactor
        self.consumable = consumable

        if self.consumable == True:
            self.usecounter = num_uses
        else:
            self.usecounter = 999

    def use_item(self, target):
        if type(target) == type(Person):
            target.health = target.health + self.healfactor - self.damage
            if target.health <= 0:
                target.die()
        
        if self.consumable == True:
            self.usecounter -= 1
            if self.usecounter <= 0:
                self.destroy()
    
    def destroy(self):
        pass

class Furniture:
    pass


player1 = Person('Steve')
enemy1 = Person('John')