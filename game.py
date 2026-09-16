from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Attic"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        print(f"{hero.name} attacks {enemy.name} for {hero_damage} damage!")
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            print(f"{enemy.name} attacks {hero.name} for {enemy_damage} damage!")
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name}wins!")
        print(f"{enemy.name}wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gregor")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    hero1 = Hero("Ares")
    print(f"{hero1.name} enters the arena with {hero1.health} health.")

    battle(hero1, goblin)