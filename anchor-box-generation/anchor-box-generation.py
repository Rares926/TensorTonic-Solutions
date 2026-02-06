import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """

    stride = image_size//feature_size

    g_W = image_size // stride
    g_H = image_size // stride

    all_anchors = []
    for i in range(g_H):
        for j in range(g_W):
            cx = (j+0.5) * stride
            cy = (i+0.5) * stride
            anchors_for_cell = []
            for scale in scales:
                for ar in aspect_ratios:
                    b_W = float(scale * np.sqrt(ar))
                    b_H = float(scale / np.sqrt(ar))
                    anchor_box = [
                        cx - b_W/2,
                        cy - b_H/2,
                        cx + b_W/2,
                        cy + b_H/2
                    ]
                    all_anchors.append(anchor_box)

    return all_anchors