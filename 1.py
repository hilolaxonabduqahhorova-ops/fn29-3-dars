class User:
    def __init__(self, name, phone, balance):
        self.name = name
        self._phone = phone
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, n):
        if n < 0:
            print("balans 0 yoki 0 dan kicik mumkn emas!")
        else:
            self.__balance = n
    def __str__(self):
        return f"{self.name}, balance: {self.__balance} som"
    def __repr__(self):
        return f"user(name={self.name}, phone={self._phone})"
# ---------------------------------
class Client(User):
    def __init__(self, name, phone, balance, card_number):
        super().__init__(name, phone, balance)
        self.card_number = card_number
    def deposit(self, n):
        if n > 0:
            self.balance += n
            print(f"{n} som qowildi balansga")
        else:
            print("qowilayotgan summa 0 dan katta boliwi kerak")
    def withdraw(self, n):
        if n <= 0:
            print("yecib olinadigon summa 0 dan katta boliwi kerak")
        elif n > self.balance:
            print("hisobingizda mablag yetarli emas!!")
        else:
            self.balance -= n
            print(f"{n} som muvaffaqiyatli yecildi")
    def info(self):
        print(f"mijoz: {self.name}, talefon: {self._phone}, karta raqam: {self.card_number}, balans: {self.balance}")
# ------------------------------
class Employee(User):
    def __init__(self, name, phone, balance, employee_id, salary):
        super().__init__(name, phone, balance)
        self.employee_id = employee_id
        self.salary = salary
    def work(self):
        print(f"{self.name} bank xodimi sifatida iwlayapti")
    def info(self):
        print(f"xodim: {self.name}, telefon: {self._phone}, employee ID: {self.employee_id}, maow: {self.salary} som")
# -------------------------------
class Bank:
    def __init__(self):
        self.clients = []
        self.employees = []
    def add_clients(self, client):
        self.clients.append(client)
    def add_employees(self, employee):
        self.employees.append(employee)
    def show_client(self):
        print("\n---hamma mijoz ---")
        for client in self.clients:
            print(client)
    def show_employee(self):
        print("\n--- hama xodim ---")
        for employee in self.employees:
            print(employee)
    def find_client(self, n):
        for client in self.clients:
            if client._phone == n or client.card_number == n:
                return client
        return None
# ----------------------------------
bank = Bank()
c1 = Client("hasan", "345678", 134567, "234567890")
c2 = Client("husan", "4567890", 87654, "3456789")
c3 = Client("toxir", "3456789", 987654, "34567890")
e1 = Employee("sabin", "345678", 0, "3456", 876543)
e2 = Employee("ali", "876543", 0, "34576", 234567)
bank.add_clients(c1)
bank.add_clients(c2)
bank.add_clients(c3)
bank.add_employees(e1)
bank.add_employees(e2)
print("\n--- qowiw ---")
c1.deposit(500000)
print("\n--- ciqariw---")
c2.withdraw(300000)
print("\n--- bans---")
print(f"{c1.name} balans: {c1.balance} som")
print(f"{c2.name} balans: {c2.balance} som")
bank.show_client()
bank.show_employee()
print("\n--- polimarfizm ---")
users = [
    c1,
    c2,
    e1,
    e2
]
for user in users:
    user.info()
print("\n--- work ---")
e1.work()
e2.work()
print("\n--- str ---")
print(str(c1))
print("\n--- repr ---")
print(repr(c1))
print("\n--- encapsuletion ---")
print("private - balance tashqaridan togridan-togri olinmaydi.")
print("balans bilan property orqali iwlaymiz:", c1.balance)
print("\n--- FIND CLIENT ---")
found = bank.find_client("345678")
if found:
    print("mijoz topildi:")
    found.info()
else:
    print("mijoz topilmadi.")