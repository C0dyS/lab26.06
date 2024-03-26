class Animal:
    def __init__(self,name,age,weight_kg):
        self._name = name
        self._weight_kg = weight_kg
        self._age = age
    def get_data(self):
        return self._name,self._age,self._weight_kg
    def change_age(self,new_age):
        self._age = new_age
    def change_weight(self,new_weight_kg):
        self._weight_kg = new_weight_kg
    def eat(self,food_in_kg):
        self._weight_kg += food_in_kg
    def change_name(self,new_name):
        self._name = new_name
class Tiger(Animal):
    def __init__(self,name,age,weight_kg):
        super().__init__(name,age,weight_kg)
    def Pounce(self):
        print('Pounce')
    def Look_majestic(self):
        print('tiger looks majestic')
class Crocodile(Animal):
    def __init__(self,name,age,weight_kg):
        super().__init__(name,age,weight_kg)
    def sleep(self):
        print('crocodile sleeps')
class Kangaroo(Animal):
    def __init__(self,name,age,weight_kg):
        super().__init__(name,age,weight_kg)
    def jump(self):
        print('Kangaroo jumps')
