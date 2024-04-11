class Character:
    def __init__(self, name, race, level=1):
        self.name = name
        self.race = race
        self.level = level

    def level_up(self):
        self.level += 1

    def show_info(self):
        print(f"Name: {self.name}\nRace: {self.race}\nLevel: {self.level}")


class Knight(Character):
    def __init__(self, name, race, weapon):
        super().__init__(name, race)
        self.weapon = weapon 

    def special_ability(self):
        print(f"{self.name} swings their {self.weapon} mightily!")


class Wizard(Character):
    def __init__(self, name, race, magic_type):
        super().__init__(name, race)
        self.magic_type = magic_type

    def special_ability(self):
        print(f"{self.name} casts a powerful {self.magic_type} spell!")


hayden = Knight("Hayden", "Human", "Sword")
sekol = Wizard("Sekol", "Human", "Red Lightsaber")

hayden.show_info()
hayden.special_ability()

sekol.show_info()
sekol.special_ability()
sekol.level_up()
sekol.show_info()
