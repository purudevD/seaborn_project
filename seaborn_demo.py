import math
import random
import re
import math

# This is also a demo for GIT
print('This is working great!!!')

sentence = "Ram is 12 years old and Ravi is 100 years"
pattern = re.compile(r'\d+')
matches  = pattern.finditer(sentence)
numbers = [float(match.group(0)) for match in matches]

vol_spheres = [round(4/3 * math.pi * r ** 3, 3) for r in numbers]
print(f'This is the vol of sphere = {vol_spheres}')
r = 100
print(f'The vol of sphere when r = {r} is {4/3 * math.pi * r ** 3}')
