# pip install seaborn

from matplotlib.colors import ListedColormap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def my_palplot(pal, size=1, ax=None, aspect="auto"):
    """Plot the values in a color palette as a horizontal array.
    Parameters
    ----------
    pal : sequence of matplotlib colors
        colors, i.e. as returned by seaborn.color_palette()
    size :
        scaling factor for size of plot
    ax :
        an existing axes to use
    """

    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    n = len(pal)
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(n * size, size))
    ax.imshow(np.arange(n).reshape(1, n),
              cmap=mpl.colors.ListedColormap(list(pal)),
              interpolation="nearest", aspect=aspect)
    ax.set_xticks(np.arange(n) - 0.5)
    ax.set_yticks([-0.5, 0.5])
    # Ensure nice border between colors
    ax.set_xticklabels(["" for _ in range(n)])
    # The proper way to set no ticks
    ax.yaxis.set_major_locator(ticker.NullLocator())
    fig = ax.get_figure()

    return fig, ax

gyr = [
    '#0F849F',
    '#BEE2EB',
    '#4860BA',
    '#3898AE',
    '#3DC962',
    '#71DC8D',
    '#008D25',
    '#2125ff',
    '#fa1b44',
    '#ffda21',
    '#FFFFFF',
    '#222222',
    '#666666'
    ]

fig, ax = my_palplot(sns.color_palette(gyr), size=1.5, aspect="equal")

ax.set_axis_off()

for i, name in enumerate(gyr):
    ax.text(i-0.4, 0.7, name, fontsize=10)

fig.tight_layout()

fig.savefig("color-palette.png")
plt.show()