import math

# 1a) Create a function which takes a string and concatenates
# "@gmail.com" to this string before returning it
def emailer(word):
    return word+ "@gmail.com"


# 1b) call and print this function on your name
Email= emailer("Oluwamayowa")
print(Email)

# 2a) Fix the function below. It should take in a radius and calculate
# the area of a circle (pi * radius ^ 2)
def areaCirc(rad):
    return math.pi * (rad ** 2)

# 2b) use this function to calc the area of a circle with a radius of 5
# (answer should be ~78.5398)
radius=5
area= areaCirc(radius)
print(area)

# 3a) Create a function that converts kilometers to miles
# there are roughly 1.61 km in one mile
def km_to_miles(kilometers):
    miles = kilometers / 1.61
    return miles

# 3b) use this function to convert 10km to miles
distance_in_km = 10
distance_in_miles = km_to_miles(distance_in_km)
print(distance_in_miles)
