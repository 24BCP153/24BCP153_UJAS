class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year


d1 = Date(18, 4, 2025)
d2 = Date(18, 4, 2025)
print("Dates are equal?" , d1 == d2)
