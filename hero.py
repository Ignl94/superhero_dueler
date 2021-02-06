import random
from ability import Ability
from armor import Armor


class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def fight(self, opponent):
        fighters = [self.name, opponent.name]
        winner = random.choice(fighters)
        print(f"{winner} won!")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        defense_amount = self.defend()
        defense_amount = self.defend()
        damage_taken = damage - defense_amount
        self.current_health -= damage_taken

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

# --------------------- BOTTOM ------------------------


if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
