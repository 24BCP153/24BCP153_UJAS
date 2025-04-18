class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hour = total_minutes // 60
        total_minutes = total_minutes % 60
        total_hours = self.hours + other.hours + extra_hour
        return Time(total_hours, total_minutes)

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")


t1 = Time(2, 45)
t2 = Time(1, 30)
t3 = t1.add(t2)
t3.display()
