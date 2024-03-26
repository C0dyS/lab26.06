class Human:
    def __init__(self,name,age,sex):
        self._name = name
        self._age = age
        self._sex = sex
    def get_data(self):
        return self._name,self._age,self._sex

class Builder(Human):
    def __init__(self,name,age,sex,amount_of_buildings_built):
        super.__init__(name,age,sex)
        print('parent init')
        self._amount_of_buildings_built = amount_of_buildings_built
    def get_data(self):
        name,age,sex = super().get_data()
        return name,age,sex,self._amount_of_buildings_built
class Sailor(Human):
    def __init__(self, name, age, sex, biggest_fish_caught):
        super.__init__(name, age, sex)
        print('parent init')
        self._biggest_fish_caught = biggest_fish_caught
class Pilot(Human):
    def __init__(self, name, age, sex,amount_of_plane_trips):
        super.__init__(name, age, sex)
        print('parent init')
        self._amount_of_plane_trips = amount_of_plane_trips

