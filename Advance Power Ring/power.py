import matplotlib.pyplot as plt
import numpy as np

p = 78 
fig, ax = plt.subplots(figsize=(4,4))
ax.set_facecolor( "black" )
t = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(t), np.sin(t), color = 'gray' , lw=8, alpha=0.3)

a= np.lin
