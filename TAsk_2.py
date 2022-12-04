class Hero:
    def __init__(self, name, health, armour, attac, rank):
        self.name = name
        self.health = health
        self.armour = armour
        self.attac = attac
        self._rank = rank
    def print_info(self):
        print(f"Уровень здоровья - {self.health}")
        print(f"Класс брони - {self.armour}\n")

    def getrank(self):
        return f"Ранг героя - {self._rank}"

    def setrank(self):
        self._rank = self
        return f"Теперь у героя {self.name} ранг - {self._rank}"

    def delrank(self):
        self._rank = ''
        return f"Герой проиграл, его звание обнуляется"
class Magician(Hero):
    def hello(self):
        print(f"Поприветствуйте война {self.name}")
    def attack(self, enemy):
        print(f"Маг аттакует противника {enemy} и наносит ему урон {self.attac}")
