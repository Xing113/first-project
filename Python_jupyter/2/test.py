import numpy as np
import matplotlib.pyplot as plt

print("NumPy:", np.__version__)
print("Matplotlib:", plt.matplotlib.__version__)

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Test")
plt.show()