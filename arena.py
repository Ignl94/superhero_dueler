from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name?")
        max_damage = input("What is the max damage?")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?")
        max_damage = input("What is the max damage?")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name?")
        max_block = input("What is the max block?")
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name:")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability \n[2] Add Weapon\n[3] Add Armor\n[4] Done Adding Items \n\nYour Choice:")
            if add_item == "1":
                ability = hero.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = hero.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = hero.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(
            input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(
            input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)
