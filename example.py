import presalytics
import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.rand(30)
y = np.random.rand(30)
z = np.random.rand(30)
 
fig, ax = plt.subplots()

ax.scatter(x, y, s=z*1000, alpha=0.5)

example = presalytics.MatplotlibResponsiveFigure(fig, "BubbleChart")
