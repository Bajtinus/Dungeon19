class Player:
    def __init__(self):
        self.icon = ...
        self.level = 1
        self.experience = 0

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
            if self.limits[attribute] > getattr(self, attribute) + delta:
                return False
            setattr(self, attribute, getattr(self, attribute) + delta)



class Novice(Player):
    upgrades: [
        {"cost" : 1, "stats" : {"attack" : 1}},
    ]
    def __init__(self):
        super().__init__()


