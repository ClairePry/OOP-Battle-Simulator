import random

class Boss:
    def __init__(self, name):
        self.name = name
        self.health = 160
        self.attack_power = 20

    def attack(self):
        return random.randint(5, self.attack_power)
    print("Fire ball!")

    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health=0


    def is_alive(self):
        return self.health > 0

    def battle_cry(self):
        print(f"{self.name} Power attack!")