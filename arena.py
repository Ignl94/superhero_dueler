from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena():
    def __init__(self):
        self.team_one = list()  # None wouldn't allow me to append my hero to self.teams
        self.team_two = list()

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
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(
            input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            # add_hero in team.py not working so replaced with append
            self.team_one.append(hero)

    def build_team_two(self):
        numOfTeamMembers = int(
            input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            # add_hero in team.py not working so replaced with append
            self.team_two.append(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"{self.team_one.name} average K/D was: {str(team_kills/team_deaths)}")
        print("\n")
        team_2_kills = 0
        team_2_deaths = 0
        for hero in self.team_two.heroes:
            team_2_kills += hero.kills
            team_2_deaths += hero.deaths
        if team_2_deaths == 0:
            team_2_deaths = 1
        print(f"{self.team_two.name} average K/D was: {str(team_kills/team_deaths)}")

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived form " + self.team_two.name + ": " + hero.name)


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False

        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
