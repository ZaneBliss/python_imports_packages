from appliances import DishWasher
from appliances import Dryer
from appliances import Washer
from appliances import CanOpener
from appliances import CoffeeMaker
from appliances import DishWasher
from appliances import Dryer
from appliances import Refrigerator
from appliances import Stove
from appliances import Washer

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

can = CanOpener("black")
can.open_can()