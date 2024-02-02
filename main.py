

class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 0
        self.inventory = []
        self.equipped_item = self.inventory[0]
    
    def equip_item(self, selection):
        selection.lower()
        if selection in self.inventory:
            self.equipped_item = self.inventory[self.inventory.index(selection)]
        else:
            print('Item not found in inventory, did you mistype?')
    
    def attack(self):
        pass

    def grab_item(self):
        pass

    def search_area(self):
        pass

class Room:
    def init(self, furniture = None, items = None, connected_doors = None):
        if furniture is None:
            furniture = []
        
        if items is None:
            items = []
        
        if connected_doors is None:
            connected_doors = {}

        self.furniture = furniture
        self.items = items
        self.connected_doors = connected_doors

