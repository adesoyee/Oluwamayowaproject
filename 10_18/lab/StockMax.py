# TODO: Get StockData from the StockData.py file
from StockData import StockData

class StockMax(StockData): 
    def find_max_value(self):
        # TODO: implement a method that will convert each data point into a float
        # ignore date & missing values
        # and extract the maximum value of each list
        max_values = []
        for row in self.data:
            values = [float(value) for value in row[1:] if value]
            if values:
                max_value = max(values)
                max_values.append(max_value)
            else:
                max_values.append(None)
        return max_values