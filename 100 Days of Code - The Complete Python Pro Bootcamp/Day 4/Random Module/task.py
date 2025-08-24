import random
import my_module

# random integer
random_integer = random.randint(1, 10)
print(random_integer)

# module
print(my_module.my_favorite_number)

# random float
random_float = random.random() # in between 0.0 (inclusive) and 1 (exclusive)
print(random_float)

random_float2 = random.random() * 10 # in between 0 and 10 (exclusive)
print(random_float2)

# random uniform
random_uniform = random.uniform(1, 10) # in between 1 and 10 both inclusive
print(random_uniform)

# Pause 1
random_number = random.randint(1, 2)

if random_number == 1:
    print("Heads")
else:
    print("Tails")