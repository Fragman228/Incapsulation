class Bankaccount:
    def __init__(self, name, balance, passport, password):
        self.__password = password
        self.__name = name
        self._balance = balance
        self._passport = passport

    def getbalance(self):
        return f"Баланс вашего счета - {self._balance}"

    def getpassport(self):
        return f"Данные вашего пасспорта - {self._passport}"

    def setpassword(self):
        self.__password = self
        return f"Вы изменили пароль. Чтобы его узнать запросите его"

    def setpassport(self):
        if self == self.__password:
            self.__password = input("Введите новые данные пасспорта")
            return "Вы успешно заменили данные паспорта"
        else:
            return "Вы ввели неправильные пароль, повторите попытку"

    def setbalance(self):
        self._balance = input()
        if int(self._balance) < 0:
            self._balance = 0
            print("Ваш баланс равен нулю")
        else:
            'Колво денег заменено'

    def delpassport(self):
        if self == self.__password:
            self._passport = None
            return "Вы успешно удалили данные паспорта"
        else:
            return "Вы ввели неправильные пароль, повторите попытку"
