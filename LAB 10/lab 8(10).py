import string

with open("input.txt", "r") as infile:
    text = infile.read()

remove_words = ["a", "an", "the"]

for p in string.punctuation:
    text = text.replace(p, "")


words = text.split()


new_words = []

for word in words:
    if word.lower() not in remove_words:
        new_words.append(word)


new_text = ' '.join(new_words)


with open("output.txt", "w") as outfile:
    outfile.write(new_text)

print("Finished! Check 'output.txt'")

