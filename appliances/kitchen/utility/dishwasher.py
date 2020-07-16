from appliances import Appliance

class DishWasher(Appliance):

    def __init__(self, color):
        super().__init__(self, color)

    def wash_dishes(self):
        print("grind, grind, clunk. Time to call the repair person")

