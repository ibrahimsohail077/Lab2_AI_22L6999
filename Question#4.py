
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
X = np.array(iris.data)
Y = np.array(iris.target)


means = np.mean(X, axis=0)
medians = np.median(X, axis=0)
stds = np.std(X, axis=0)

print("Means:", means)
print("Medians:", medians)
print("Standard Deviations:", stds)


mins = np.min(X, axis=0)
maxs = np.max(X, axis=0)

print("Minimums:", mins)
print("Maximums:", maxs)


sepal_features = X[:, :2]  
print("\nSepal Length and Sepal Width:\n", sepal_features)


# 2. Matplotlib visualizations

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=Y) 
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.show()



plt.figure(figsize=(8, 6))
plt.hist(X[:, 0], bins=10, edgecolor='black')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")
plt.show()


plt.figure(figsize=(8, 6))
plt.plot(X[:, 2], X[:, 3], marker='o', linestyle='-')
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.show()
