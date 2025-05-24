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


class Game():
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self):
        print("Начинается битва героев!")
        print(
            f"{self.player.name} (Здоровье: {self.player.health}) vs {self.computer.name} (Здоровье: {self.computer.health})")

        current_round = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {current_round}")

            # Ход игрока
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья")

            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья")

            current_round += 1

        # Определение победителя
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")
        print("Игра окончена!")


player_name = input("Введите имя вашего героя: ")
player = Hero(player_name)
computer = Hero("Компьютерный герой")

game = Game(player, computer)
game.start()
