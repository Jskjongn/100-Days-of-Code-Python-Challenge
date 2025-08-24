import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# random choice
print(random.choice(friends))

random_name = random.randint(0, len(friends) - 1)
print(friends[random_name])
