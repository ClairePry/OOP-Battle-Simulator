from goblin import Goblin
from hero import Hero
from boss import Boss

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
        print(f"{hero.name} wins!")

    if enemy.is_alive():
        print(f"{enemy.name} wins!")

def bossFight(hero: Hero, boss: Boss):
    while hero.is_alive() and boss.is_alive():
        hero_damage = hero.attack()
        print(f"{hero.name} attacks {boss.name} for {hero_damage} damage!")
        boss.take_damage(hero_damage)

        if boss.is_alive():
            boss_damage = boss.attack()
            print(f"{boss.name} attacks {hero.name} for {boss_damage} damage!")
            hero.take_damage(boss_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")

    if boss.is_alive():
        print(f"{boss.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gregor")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    print("But no hero has answered the call... yet.")
    hero1 = Hero("Ares")
    hero1.battle_cry()
    print(f"{hero1.name} enters the arena with {hero1.health} health.")
    battle(hero1, goblin)

    print()
    print(f"A terrible presence enters the {ARENA_NAME}")
    boss = Boss("King Gorger")
    boss.battle_cry()
    print(f"{boss.name} enters the {ARENA_NAME} with {boss.health} health")

    bossFight(hero1, boss)

if __name__ == "__main__":
    main()
