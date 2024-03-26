class Clock:
    def __init__(self,hours,minutes,):
        self._minutes = minutes
        self._hours = hours
    def get_data(self):
        return self._hours,self._minutes
    def change_minutes(self,new_minutes):
        self._minutes = new_minutes
    def change_hours(self,new_hours):
        self._hours = new_hours
class AnalogClock(Clock):
    def __init__(self, hours, minutes):
        super().__init__(hours, minutes)

    def display_time(self):
        if self._hours < 12:
            print(f'{self._hours}:{self._minutes} AM')
        else:
            print(f'{self._hours - 12}:{self._minutes} PM')
class DigitalClock(Clock):
    def __init__(self,hours,minutes):
        super().__init__(hours,minutes)
    def display_time(self):
        print(f'{self._hours}:{self._minutes}')

clock1 = AnalogClock(24,30)
clock2 = AnalogClock(12,00)
clock3 = DigitalClock(19,30)
clock1.display_time()
clock2.display_time()
clock3.display_time()