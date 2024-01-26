import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [1,2,3,1,2,3]
x = np.array([1,2,3,1,2,3])
# x + pd.Series(np.array([1,2,3,1,2,3]))

plt.figure(figsize=(8,4))
plt.plot(x, linewidth=2, color="green", marker="*", linestyle="dashed", label="line_1")
plt.legend()
plt.grid(color="gray", linestyle="-", linewidth=1.5)
plt.yticks()
plt.xticks()
plt.xlabel("ось фбсцисс")
plt.ylabel("ось ординат")
plt.show()