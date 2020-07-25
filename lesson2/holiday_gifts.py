import time
import numpy as np



with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')

gift_costs = np.array(gift_costs).astype(int)   # convert string to int

start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print(f"Duration: {time.time() - start} seconds")

start = time.time()

total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))

# second opt: calculate using np
start = time.time()

total_price = np.sum(gift_costs)        # TODO: compute the total price

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))


## using lambda function
start = time.time()
x = lambda x: gift_costs < 25
total_price = np.sum(x)
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))
