import numpy as np
from scipy.interpolate import make_interp_spline


def interpolate(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    x_new = np.linspace(x.min(), x.max(), 100)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_new)

    return x_new, y_smooth
