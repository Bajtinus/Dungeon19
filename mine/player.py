from PyQt6.sip import delete


class Player:
    def __init__(self):
        self.icon = ...
        self.level = 1
        self.experience = 0
        self.max_xp = 100

        self.keys = ...
        self.coins = ...
        self.stars = ...

        self.health = ...
        self.attack = ...
        self.defense = ...
        self.speed = ...
        self.limits = ...

    def upgrade_stats(self, upgrade: dict):
        """
        Upgrades the players stats

        :param upgrade: Dictionary in the form of {"cost" : int, "attack" : 3, "speed" : -1, ...}
        :return: False if the player does not have enough stars
        """
        cost = upgrade.pop("cost")
        if self.stars < cost:
            return False


        self.stars -= cost
        for attribute, delta in upgrade.items():
            if attribute == "speed":
                if self.limits[attribute] < getattr(self, attribute) + delta:
                    setattr(self, attribute, self.limits[attribute])
            else:
                if self.limits[attribute] > getattr(self, attribute) + delta:
                    setattr(self, attribute, self.limits[attribute])
            setattr(self, attribute, getattr(self, attribute) + delta)

    def add_xp(self, xp: int):
        self.experience += xp
        if self.experience >= self.max_xp:
            self.experience -= self.max_xp
            self.level += 1
            self.max_xp = int(self.max_xp * 1.2)


class Novice(Player):
    upgrades = [
        {"cost": 10, "health": 50},
        {"cost": 10, "attack": 4},
        {"cost": 10, "defense": 4},
        {"cost": 10, "speed": -2}
    ]
    
    def __init__(self):
        super().__init__()
        self.keys = 3
        self.coins = 200
        self.stars = 30
        
        self.health = 250
        self.attack = 25
        self.defense = 10
        self.speed = 40

        self.limits = {
            "health": 2000,
            "attack": 255,
            "defense": 255,
            "speed": 7
        }

