
import pip

from dice_rolling import RollBuilder

def dice (x):
    x = ("builder")
    return x 
builder = RollBuilder()
builder.set_amount_of_dice(2)
builder.set_number_of_sides(6)
builder.build()

print(builder.get_result())


