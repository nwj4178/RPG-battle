# battle.py

class Battle:
    def fight(self, hero, monster):
        print(f"\nThe battle between {hero.name} and {monster.name} begins!")

        while hero.is_alive() and monster.is_alive():
            # Hero attacks first
            damage = monster.take_damage(hero.attack)
            print(f"{hero.name} attacks {monster.name} for {damage} damage!")

            if not monster.is_alive():
                print(f"{monster.name} is defeated!")
                break

            # Monster counterattacks
            damage = hero.take_damage(monster.attack)
            print(f"{monster.name} attacks {hero.name} for {damage} damage!")

            if not hero.is_alive():
                print(f"{hero.name} has been defeated by {monster.name}.")
                break
