from goblin import Goblin
from boss import Boss

enemies = [
    Goblin("Gribble"), Boss("King Gorger"),
]

for enemy in enemies:
    print(f"{enemy.name} enters with {enemy.health} health")

    damage = enemy.attack()
    print(f"{enemy.name} attacks for {damage} damage!")

    enemy.take_damage(20)
    print(f"Alive: {enemy.is_alive()}!")   