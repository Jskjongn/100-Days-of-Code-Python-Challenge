# range function
for number in range(1,10): # actually 1-9 as 10 is exclusive, would need to be 1-11 to get 10
    print(number)

for number in range(1, 11, 3): # steps by 3 from the number it lands on
    print(number)

# Pause 1
total = 0
for number in range(1, 101):
    total += number
print(total)