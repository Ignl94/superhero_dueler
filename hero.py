import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        if self.abilities == []:
            print("Draw!")
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                hero_attack = self.attack()
                opponent.take_damage(hero_attack)
                opponent.is_alive()
                if opponent.current_health <= 0:
                    self.add_kills(1)
                    opponent.add_deaths(1)
                    print(f"{self.name} Won!")
                    break
                opponent_attack = opponent.attack()
                self.take_damage(opponent_attack)
                self.is_alive()
                if self.current_health <= 0:
                    opponent.add_kills(1)
                    self.add_deaths(1)
                    print(f"{opponent.name} Won!")
                    break

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

# --------------------- BOTTOM ------------------------


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
