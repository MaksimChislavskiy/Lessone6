class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f'{self.name} атакует {other.name} и наносит {self.attack_power} урона')


    def is_alive(self):
        return self.health > 0


hero1 = Hero('Герой 1')
hero2 = Hero('Герой 2')

hero1.attack(hero2)
