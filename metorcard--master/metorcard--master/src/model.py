from collections import defaultdict

class MetroCard:
    def __init__(self, card_id, balance):
        self.id = card_id
        self.src = None
        self.balance = int(balance)
        self.used_discount = False

    def add_balance(self, amount):
        self.balance += amount

    def update_src(self, src):
        self.src = src


class Station:
    def __init__(self, name):
        self.name = name
        self.total_amount = 0
        self.discount = 0
        self.passenger_history = defaultdict(int)

    def add_amount(self, amount):
        self.total_amount += amount

    def add_discount(self, amount):
        self.discount += amount

    def add_passenger(self, passenger_type):
        self.passenger_history[passenger_type] += 1
