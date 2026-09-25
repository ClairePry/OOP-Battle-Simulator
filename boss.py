from enemy import Enemy




class Boss(Enemy):

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=30)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} Strong attack!")
        return damage + bonus_damage

    def battle_cry(self):
        print(f"{self.name} get crushed!")