# Random walk (R3: reproducible)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C. Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.1 / macOS 10.12.4 / 64 bits architecture
import random

def walk():
    path = []
    x = 0
    for i in range(10):
        if random.uniform(-1,+1) > 0:
            x = x + 1
        else:
            x = x - 1
        path.append(x)
    return path

# Unit test
random.seed(1)
assert walk() == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]

# Random walk for 10 steps
seed = 1
random.seed(seed)
path = walk()

# Display & save results
print(path)
results = {'data': path, 'seed': seed}
with open("results-R3.txt", "w") as fd:
    fd.write(str(results))