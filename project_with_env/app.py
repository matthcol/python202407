import numpy as np

values = np.random.normal(10, 2.5, 1000)
print("Count:", len(values))
print("Mean:", values.mean())
print("Std:", values.std())