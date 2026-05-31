import matplotlib.pyplot as plt
import numpy as np

angle = np.pi/3
theta = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(theta), np.sin(theta), linewidth=3)
plt.arrow(0, 0, np.cos(angle), np.sin(angle), head_width=0.1, color='red')
plt.text(0,1.1,"N")
plt.text(1.1,0,"E")
plt.text(0,-1.2,"S")
plt.text(-1.2,0,"W")
plt.axis('equal')
plt.axis('off')
plt.title(" Compass ")

plt.show()