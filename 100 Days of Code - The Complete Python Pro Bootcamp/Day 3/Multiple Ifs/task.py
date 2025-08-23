print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price = 0

if height >= 120:
    print("You can ride the rollercoaster")

    # checks age
    age = int(input("What is your age? "))
    if age <= 12:
        price = 5
        print("Child tickets are $5.")
    elif age <= 18:
        price = 7
        print("Child tickets are $7.")
    else:
        price = 12
        print("Child tickets are $12.")

    # if yes then extra $3
    photo = input("Do you want a photo? (Y/N): ")
    if photo == "Y":
        price += 3

    # prints total
    print("Your total is $", price)
else:
    print("Sorry you have to grow taller before you can ride.")
