import math
try:
    print("The exponential value is")
    print(math.exp(1000))
    
except OverflowError as oe:
    print("After overflow", oe)