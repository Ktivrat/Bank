# ЗАДАНИЕ 1 (Обязательно) 
# на выбор два класса

# Создать класс кошелек с атрибутами в виде:

# 1 баланс +
# 2 увелечение баланса на n +
# 3 Сравнение двух кошельков +
# 4 проверку баланса на ноль +
# 5 предложить ваш метод -


class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        
    # Показ баланса 
    def show_balance(self):
        print(f'Имя клиента: {self.__name} - Баланс клиента: {self.__balance}')
        
    # Увеличение баланса
    def deposit(self, amount):
        self.__balance += amount
        print(f"Баланс счета увеличен на {amount}. Новый баланс: {self.__balance}\n")
        
    # проверка баланса    
    def check(self):
        if self.__balance == 0:
            print(f'Баланс пользователя {self._Bank__name} равен 0')   
        
      # Сравнения  
    def compare_balance(self, other):
        if self > other:
            return f'Баланс клиента {self._Bank__name} больше чем у {other._Bank__name}'
        elif self < other:
            return f'Баланс клиента {other._Bank__name} больше чем у {self._Bank__name}'
        else:
            return 'Оба счета равны по сумме'
        
        # Методы сравнения (О которых я в душе не чаял, но оказывается без них ничего не работает -_____-)
        # Мы либо не проходили такое, либо я слушал одним местом...
        
    def __eq__(self, other): #определяет поведение оператора равенства ==. 
        return self.__balance == other.__balance

    def __gt__(self, other): #определяет поведение оператора >. 
        return self.__balance > other.__balance

    def __lt__(self, other): #определяет поведение оператора <
        return self.__balance < other.__balance
    
    

# Создаем клиентов
client1 = Bank('Александр', 1200)
client2 = Bank('Виктор', 125)
client3 = Bank('Константин', -500)

client1.show_balance()
client1.deposit(500.0)
client1.check()

client2.show_balance()
client2.deposit(500.0)
client2.check()

client3.show_balance()
client3.deposit(500.0)
client3.check()

# Вывод сравнения
clients = [client1, client2, client3,]

for i in range(len(clients)):
    for j in range(i + 1, len(clients)):
        result = clients[i].compare_balance(clients[j])
        print(result)
        
        
# Сначала вывел так, но подумал, что если их будет много, то будет проблема
    
    # comparison_result = client1.compare_balance(client2)
    # comparison_result_3 = client1.compare_balance(client3)
    # print(comparison_result)
    # print(comparison_result_3)