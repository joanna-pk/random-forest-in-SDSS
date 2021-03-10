"""support_tools.py

Collection of useful functions to help
with data visualisation in the random forest
tutorial
"""
__version__ = 0.0
__author__ = 'Joanna Piotrowska'

# ==================================================================
# imports
# ==================================================================
from matplotlib import rcParams

# ==================================================================
# python function definitions
# ==================================================================
def configure_plots():
    """
    Setting global Matplotlib settings for plots
    """
    # line settings
    rcParams['lines.linewidth'] = 2
    rcParams['lines.markersize'] = 3
    rcParams['errorbar.capsize'] = 3

    # tick settings
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['xtick.minor.visible'] = True
    rcParams['ytick.minor.visible'] = True
    rcParams['xtick.major.size'] = 7
    rcParams['xtick.minor.size'] = 4
    rcParams['xtick.direction'] = 'in'
    rcParams['ytick.major.size'] = 7
    rcParams['ytick.minor.size'] = 4
    rcParams['ytick.direction'] = 'in'

    # text settings
    rcParams['mathtext.rm'] = 'serif'
    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 14
    rcParams['text.usetex'] = True
    rcParams['axes.titlesize'] = 18
    rcParams['axes.labelsize'] = 15
    rcParams['axes.ymargin'] = 0.5

    # legend
    rcParams['legend.fontsize'] = 12
    rcParams['legend.frameon'] = False

    # grid in plots
    rcParams['grid.linestyle'] = ':'

    # figure settings
    rcParams['figure.figsize'] = 8, 5
    rcParams['savefig.format'] = 'pdf'
