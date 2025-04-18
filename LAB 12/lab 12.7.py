class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters


w = Weather(["Rain", "Sunny", "Cloudy"])
print("Sunny" in w)
print("Snow" in w)
