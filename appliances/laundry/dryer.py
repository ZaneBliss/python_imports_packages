from appliances import Appliance

class Dryer(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def dry_clothes(self, setting="low"):
        if setting != "low":
          print("Please allow 40 minutes for you clothes to come out crispy.")
        else:
          print("Please allow 40 minutes for your clothes to come out soggy.")
