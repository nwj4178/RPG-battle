# character.py

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.hp -= actual_damage
        return actual_damage

    def __str__(self):
        return f"{self.name}: HP={self.hp}, Attack={self.attack}, Defense={self.defense}"

class Hero(Character):
    def __init__(self, name, hp, attack, defense, role):
        super().__init__(name, hp, attack, defense)
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role}): HP={self.hp}, Attack={self.attack}, Defense={self.defense}"

class Monster(Character):
    pass
