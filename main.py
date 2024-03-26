class Passport:
    def __init__(self,name,age,id_number):
        self._name = name
        self._age = age
        self._id_number = id_number
    def get_data(self):
        return self._name,self._age,self._id_number
    def change_id_number(self,new_id_number):
        self._id_number = new_id_number

class ForeignPassport(Passport):
    def __init__(self,name,age,foreign_passport_id_number):
        super().__init__(name,age,'')
        print('parent init')
        self._foreign_passport_id_number = foreign_passport_id_number
    def get_data(self):
        name,age, _ = super().get_data()
        return name,age,self._foreign_passport_id_number
    def change_foreign_id_number(self,new_id_number):
        self._foreign_passport_id_number = new_id_number