import csv


class StockData:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_csv(self):
        with open(self.filename, 'r') as file:
            # TODO: Use the csv.reader function to read the contents of the file
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                self.data.append(row)

    def calculate_lengths(self):
        lengths = []
        for row in self.data:
            # TODO: Count the number of non-empty items in each row
            # and append the count to the lengths list
            # also be sure to ignore the date value in this list
            length = sum(1 for item in row [1:] iff item)
            lengths.append(length)
        return lengths


# Part 2: Instantiate the StockData class and call its methods
# TODO: Create an instance of StockData with the filename 'stock_data.csv'
stock_data = StockData('stock_data.csv')

# TODO: Call the read_csv method of the instance
stock_data.read_csv()

# TODO: Print the data attribute of the instance
print("Stock Data:")
for row in stock_data.data:
    print(row)

# TODO: Call the calculate_lengths method and print the result
lengths = stock_data.calculate_lengths()
print("Lengths of each row (excluding date):", lengths)