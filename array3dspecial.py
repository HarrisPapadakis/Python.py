import numpy as np

# Matrix μηδενικών
zeros = np.zeros((3, 3))
print("Zeros:\n", zeros)

# Matrix μονάδων
ones = np.ones((3, 3))
print("\nOnes:\n", ones)

# Identity Matrix
identity = np.eye(3)
print("\nIdentity matrix:\n", identity)

# Array γεμάτο με συγκεκριμένη τιμή
full = np.full((3, 3), 7)
print("\nFull:\n", full)

# Array με ακολουθία αριθμών
arange = np.arange(0, 10, 2)
print("\nArange:\n", arange)

# Array με ίσες αποστάσεις
linspace = np.linspace(0, 1, 5)
print("\nLinspace:\n", linspace)