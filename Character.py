class Character(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def change_name(self, name):
        self.name = name

    def change_health(self, health):
        self.health = health

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def mod_health(self, mod):
        self.health += mod


class Ranger(Character):
    def __init__(self, name, health, family):
        self.family = family
        Character.__init__(self, name, health)

    def change_family(self, family):
        self.family = family

    def get_family(self):
        return self.family


class Wizard(Character):
    def __init__(self, name, health, family):
        self.family = family + " The Mega Epic"
        Character.__init__(self, name, health)

    def change_family(self, family):
        self.family = family

    def get_family(self):
        return self.family


class Bard(Character):
    def __init__(self, name, health, family):
        self.family = family + " Tuniest Tunester"
        Character.__init__(self, name, health)

    def change_family(self, family):
        self.family = family

    def get_family(self):
        return self.family


class Paladin(Character):
    def __init__(self, name, health, family):
        self.family = family + " The POG"
        Character.__init__(self, name, health)

    def change_family(self, family):
        self.family = family

    def get_family(self):
        return self.family


class Barbarian(Character):
    def __init__(self, name, health, family):
        self.family = family + " The Stronk"
        Character.__init__(self, name, health)

    def change_family(self, family):
        self.family = family

    def get_family(self):
        return self.family
