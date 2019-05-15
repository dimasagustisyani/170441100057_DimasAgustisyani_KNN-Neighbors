from sklearn.datasets import load_iris

iris = load_iris()

iris

x_index = 0

y_index = 1

from matplotlib import pyplot as plt

formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])