"""
Heatmap.py
=====================
Generate heatmap for Pandas series
"""

import pandas as pd
import matplotlib.cm


def getHex(cmap, val):
    """
    Get hex color, given numeric value.
    :param cmap: Matplotlib colormap
    :type cmap: matplotlib.cm
    :param val: Numeric value
    :type val: float, int
    """

    val_rgb = cmap(val)[:3]
    val_hex = matplotlib.colors.rgb2hex(val_rgb)
    
    return val_hex


def LinearHeatmap(value, max):
    """
    Generate heatmapped series, given numeric series in Pandas.
    :param series: Pandas series with numeric values
    :type series: Pandas series
    """

    # generate colormap
    cmap = matplotlib.cm.get_cmap('plasma')

    # linear heatmap
    color = getHex(cmap, 1 - (value / max))
    
    return color
