import math
import numpy as np
test_scores = [88, 92, 79, 93, 85]

def flat_curve(arr, n):
    return [i + n for i in arr]
def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]

curved_5= flat_curve(test_scores, 5)
curved_10= flat_curve(test_scores, 10)
curved_sqrt= square_root_curve(test_scores)
for score_list in curved_5, curved_10, square_root_curve:
    print(score_list)
