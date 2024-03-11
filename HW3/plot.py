import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

ax.plot()

ax.add_patch(Rectangle((2, 1), 12, 16, edgecolor='k', facecolor='0.9', zorder=1))
ax.add_patch(Rectangle((2, 1), 12, 16, edgecolor='k', facecolor='none', zorder=1003))
ax.text(2.25, 1.5, "Image", fontsize=12)
ax.add_patch(Rectangle((5, 10), 5, 5, edgecolor='k', facecolor='r', zorder=1001, ls='-.', alpha=0.25))
ax.text(5.25, 15.25, "Prediction", fontsize=12)
ax.add_patch(Rectangle((4, 9), 7, 5, edgecolor='k', facecolor='g', zorder=1002, ls='--', alpha=0.25))
ax.text(7.5, 8, "Ground Truth", fontsize=12)
ax.set_ylim(0, 18)
ax.set_xlim(0, 15)
ax.grid(True, which='major', linestyle='-')
ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':')

fig.savefig('plot.png', dpi=300)
