from appliances import Appliance

class Stove(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def cook_food(self):
        print("The stove cooked the food. It was well done.")
