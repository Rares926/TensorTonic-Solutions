import math
import numpy as np 

def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size features.
    """
    feature_map = np.asarray(feature_map)
    outs = []

    for roi in rois:

        roi_tl_x, roi_tl_y, roi_br_x, roi_br_y = roi

        roi_W = abs(roi_tl_x - roi_br_x)
        roi_H = abs(roi_tl_y - roi_br_y)

        out_array = np.zeros((output_size, output_size))

        for i in range(output_size):
            for j in range(output_size):

                h_start = roi_tl_y + math.floor(i * roi_H / output_size)
                h_end = roi_tl_y + math.floor((i+1) * roi_H  / output_size)

                w_start = roi_tl_x + math.floor(j * roi_W / output_size)
                w_end = roi_tl_x + math.floor((j+1) * roi_W / output_size)

                h_end = h_end if h_end != h_start else h_start + 1
                w_end = w_end if w_end != w_start else w_start + 1

                region = feature_map[
                    h_start : h_end,
                    w_start : w_end
                ]

                out_array[i,j] = region.max()

        outs.append(out_array.tolist())

    return outs