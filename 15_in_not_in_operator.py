# example of in and not in operator
favorite_fruit = input("Which is your favourite fruit")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
is_found = favorite_fruit in fruits
print(is_found)

disliked_fruit = input("Which is your very disliked fruit")
is_found =  disliked_fruit not in fruits
print(is_found)

countries = "india usa brazil japan germany france canada australia mexico italy"
country = input("where are you from?")
print(country in countries)

country = input("where do you want to go?")
print(country not in countries)
