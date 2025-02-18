import math
import converters
from converters import kg_to_lbs

print(converters.kg_to_lbs(70))
print(kg_to_lbs(100))

a = kg_to_lbs(100)
print(math.floor(a))
print(round(a))