

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