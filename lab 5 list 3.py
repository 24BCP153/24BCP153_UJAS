import random
number = [ random.randint(1,30) for i in range(50)]
generated_num = list(set(number))
print(generated_num)
