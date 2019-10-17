import math
import random

ARRAY_SIZE = 1000000
small20Sized = 10000000000000000000

# generates 1,000,000 unique ints
def generateUniqueArray():
    return random.sample( range(0,ARRAY_SIZE * ARRAY_SIZE), ARRAY_SIZE);

# generates 1,000,000 ints that are between 0 and (0.01 of 1 million)
def generate1pArray():
    return [ math.floor(random.random() * (ARRAY_SIZE//100)) for n in range(ARRAY_SIZE) ]

# generates 1,000,000 20 sized ints
def generate20intArray():
    size20_array = [small20Sized + index for index in range(ARRAY_SIZE)]
    random.shuffle(size20_array)
    return size20_array
