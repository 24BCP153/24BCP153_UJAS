class String:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        self.text += other.text
        return self

    def toLower(self):
        return self.text.lower()

    def toUpper(self):
        return self.text.upper()


s1 = String("Hello")
s2 = String(" World")
s1 += s2
print("Concatenated:", s1.text)
print("Lowercase:", s1.toLower())
print("Uppercase:", s1.toUpper())
