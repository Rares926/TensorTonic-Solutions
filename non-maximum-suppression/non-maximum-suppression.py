def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    inter_tl_x = max(box_a[0], box_b[0])
    inter_tl_y = max(box_a[1], box_b[1])

    inter_bl_x = min(box_a[2], box_b[2])
    inter_bl_y = min(box_a[3], box_b[3])

    if inter_tl_x >= inter_bl_x or inter_tl_y >= inter_bl_y:
        return 0.0

    inter_w = abs(inter_tl_x-inter_bl_x)
    inter_h = abs(inter_tl_y-inter_bl_y)

    box_a_area = abs(box_a[0]-box_a[2]) * abs(box_a[1]-box_a[3])
    box_b_area = abs(box_b[0]-box_b[2]) * abs(box_b[1]-box_b[3])

    if box_a_area == 0.0 or box_b_area == 0.0:
        return 0.0

    inter_area = inter_w * inter_h

    iou = inter_area / (box_a_area + box_b_area - inter_area)

    return float(iou)


def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # Write code here
    b_s = [(boxes[i], scores[i], i) for i in range(len(boxes))]
    b_s = sorted(b_s, key=lambda x: x[1], reverse=True)

    return_list = []

    if len(b_s)==0:
        return []

    while len(b_s) != 0:
        current_dp = b_s[0]
        return_list.append(current_dp)
        b_s.remove(current_dp)
        tmp_b_s = [
            dp for dp in b_s
            if iou(current_dp[0], dp[0]) < iou_threshold
        ]
        b_s = tmp_b_s
    return [dp[2] for dp in return_list]


