import numpy as np
import numpy.typing as npt


def nearest_neighbor_scaling(scaling: float, img_array: npt.ArrayLike) -> npt.NDArray:
    img_array = np.asarray(img_array)

    if img_array.ndim == 2:  # grayscale
        h, w = img_array.shape
        c = None
    elif img_array.ndim == 3:  # RGB
        h, w, c = img_array.shape
    else:
        raise ValueError("Unsupported image shape")

    new_h = int(round(h * scaling))
    new_w = int(round(w * scaling))

    if c is None:
        scaled = np.zeros((new_h, new_w), dtype=img_array.dtype)
    else:
        scaled = np.zeros((new_h, new_w, c), dtype=img_array.dtype)

    for i in range(new_h):
        for j in range(new_w):
            src_y = min(int(i / scaling), h - 1)
            src_x = min(int(j / scaling), w - 1)
            if c is None:
                scaled[i, j] = img_array[src_y, src_x]
            else:
                scaled[i, j, :] = img_array[src_y, src_x, :]

    return scaled