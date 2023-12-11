import csv

def get_highest_gdp(data, year):
    highest_gdp_state = None
    highest_gdp_value = float('-inf')  # Initialize to negative infinity

    for row in data:
        if row['Year'] == year:
            gdp_value = float(row['GDP'])
            if gdp_value > highest_gdp_value:
                highest_gdp_value = gdp_value
                highest_gdp_state = row['State']

    return highest_gdp_state

def get_lowest_gdp(data, year):
    lowest_gdp_state = None
    lowest_gdp_value = float('inf')  # Initialize to positive infinity

    for row in data:
        if row['Year'] == year:
            gdp_value = float(row['GDP'])
            if gdp_value < lowest_gdp_value:
                lowest_gdp_value = gdp_value
                lowest_gdp_state = row['State']

    return lowest_gdp_state

def get_state_gdp(data, state, year):
    for row in data:
        if row['State'] == state and row['Year'] == year:
            return float(row['GDP'])

    # Return a default value if the state and year combination is not found
    return None

# save each row into a list (TODO: change to your path!)
list_data = []
with open("data/state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
highest_gdp_2020 = get_highest_gdp(list_data, '2020')

print(f"The state with the highest GDP in 2020 is {highest_gdp_2020}")

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
lowest_gdp_2020 = get_lowest_gdp(list_data, '2020')

print(f"The state with the lowest GDP in 2020 is {lowest_gdp_2020}")