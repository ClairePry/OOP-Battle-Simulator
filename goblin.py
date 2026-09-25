from enemy import Enemy


class Goblin(Enemy):

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.gold = 0

    def stealGold(self, hero):
        print("Gimme the bread")
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("Get rekt noob!")
