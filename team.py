import random


class Team():
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill / Deaths: {kd}")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()
        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # --------------------------------------------------------
            fighter_1 = random.choice(living_heroes)
            fighter_2 = random.choice(living_opponents)
            while fighter_1.current_health > 0 and fighter_2.current_health > 0:
                fighter_1_attack = fighter_1.attack()
                fighter_2.take_damage(fighter_1_attack)
                fighter_2.is_alive()
                if fighter_2.current_health <= 0:
                    fighter_1.add_kills(1)
                    fighter_2.add_deaths(1)
                    print(f'{fighter_1.name} Won!')
                    living_opponents.remove(fighter_2)
                    break
                fighter_2_attack = fighter_2.attack()
                fighter_1.take_damage(fighter_2_attack)
                fighter_1.is_alive()
                if fighter_1.current_health <= 0:
                    fighter_2.add_kills(1)
                    fighter_1.add_deaths(1)
                    print(f'{fighter_2.name} Won!')
                    living_heroes.remove(fighter_1)
                    break
