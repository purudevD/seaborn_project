import math
import random
import re

# This is also a demo for GIT
print('This is working great!!!')

sentence = "Ram is 12 years old and Ravi is 100 years"
pattern = re.compile(r'\d+')
matches  = pattern.finditer(sentence)
print([match.group(0) for match in matches])
