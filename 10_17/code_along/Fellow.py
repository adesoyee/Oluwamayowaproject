# TODO: implement Fellow class that inherits from "Person"
# we just include another method called "form_group()"
# that prints out all the people that this fellow knows
# using a for-loop. Implement below
from Person import PersonClass

class fellow(PersonClass):
    def form_group(self):
        for name in self.aff:
            print(name)

if __name__ == "__main__":
    