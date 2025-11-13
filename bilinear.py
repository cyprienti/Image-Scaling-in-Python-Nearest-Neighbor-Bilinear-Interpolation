import numpy as np
import numpy.typing as npt


def bilinear_interpolation_scaling(scaling: float, img_array: npt.ArrayLike) -> npt.NDArray:
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
        scaled = np.zeros((new_h, new_w), dtype=np.float32)
    else:
        scaled = np.zeros((new_h, new_w, c), dtype=np.float32)

    for i in range(new_h):
        for j in range(new_w):
            y = i / scaling
            x = j / scaling

            x0 = int(np.floor(x))
            x1 = min(x0 + 1, w - 1)
            y0 = int(np.floor(y))
            y1 = min(y0 + 1, h - 1)

            if c is None:
                Ia = img_array[y0, x0]
                Ib = img_array[y0, x1]
                Ic = img_array[y1, x0]
                Id = img_array[y1, x1]
            else:
                Ia = img_array[y0, x0, :]
                Ib = img_array[y0, x1, :]
                Ic = img_array[y1, x0, :]
                Id = img_array[y1, x1, :]

            wa = (x1 - x) * (y1 - y)
            wb = (x - x0) * (y1 - y)
            wc = (x1 - x) * (y - y0)
            wd = (x - x0) * (y - y0)

            if c is None:
                scaled[i, j] = wa * Ia + wb * Ib + wc * Ic + wd * Id
            else:
                scaled[i, j, :] = wa * Ia + wb * Ib + wc * Ic + wd * Id

    return scaled.astype(img_array.dtype)