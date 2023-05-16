import math
berries = [
    {
        "berry_uid": "a2ddbaae-fe5a-4f10-a1ad-54521786ee35",
        # Position is in the arm frame (mm). NOTE: berries returned by the model
        # may be out of reach of the arm. The detection model does not take 
        # reachability of the arm into account.
        "position": {
            "x": 204.855,
            "y": -397.919,
            "z": 691.829,
        },
        # Bounding box is in pixel coordinates. Berry bounding boxes may overlap
        # with other berries.
        "bounding_box": {
            "x": 420, # Top left start of bbox
            "y": 380, # Top left start of bbox
            "height": 70, # How tall (y-axis) the strawberry is (pixels)
            "width": 30, # How wide (x-axis) the strawberry is (pixels)
        }
    },
    {
        "berry_uid": "a2ddbaae-fe5a-4f10-a1ad-54521786ee33",
        # Position is in the arm frame (mm). NOTE: berries returned by the model
        # may be out of reach of the arm. The detection model does not take 
        # reachability of the arm into account.
        "position": {
            "x": 124.855,
            "y": -397.919,
            "z": 671.829,
        },
        # Bounding box is in pixel coordinates. Berry bounding boxes may overlap
        # with other berries.
        "bounding_box": {
            "x": 340, # Top left start of bbox
            "y": 400, # Top left start of bbox
            "height": 70, # How tall (y-axis) the strawberry is (pixels)
            "width": 30, # How wide (x-axis) the strawberry is (pixels)
        }
    },
    {
        "berry_uid": "a2ddbaae-fe5a-4f10-a1ad-54521786ee34",
        # Position is in the arm frame (mm). NOTE: berries returned by the model
        # may be out of reach of the arm. The detection model does not take 
        # reachability of the arm into account.
        "position": {
            "x": 194.855,
            "y": -397.919,
            "z": 661.829,
        },
        # Bounding box is in pixel coordinates. Berry bounding boxes may overlap
        # with other berries.
        "bounding_box": {
            "x": 410, # Top left start of bbox
            "y": 410, # Top left start of bbox
            "height": 70, # How tall (y-axis) the strawberry is (pixels)
            "width": 30, # How wide (x-axis) the strawberry is (pixels)
        }
    }
]
from typing import Any
    
# Takes list of dictionary of all the berries detected via vision system as input
# This function sorts all the berries based on euclidean distance from image's origin
# Output is a list berry uids sorted based on euclidean distance
def select_berry(candidates: list[dict[str, Any]]) -> list[str]:
    """Orders the berries by criteria outlined above.
    
    Args:
        candidates: List of candidate berrie (see Data description)
        
    Returns:
        list[berry_uid]: Berry ordering to attempt.
    """
    unsorted_berries = []
    for i in candidates:
        unsorted_berries.append({"berry_uid":i['berry_uid'],"euclidean":math.sqrt(int(i['position']['x'])^2 + int(i['position']['x'])^2 + int(i['position']['x'])^2)})
    sorted_berries = sorted(unsorted_berries, key=lambda x:x['euclidean'])
    sorted_berries_uid_list = []
    for sb in sorted_berries:
        sorted_berries_uid_list.append(sb['berry_uid'])
    return sorted_berries_uid_list

# This is a helper function to determine the IoU between two detected berries
# It takes uids of two berries as input
# Output is IoU scale between 0 to 1
def IoU(berries, uid_box1, uid_box2):
    data_bb1 = next(item['bounding_box'] for item in berries if item["berry_uid"] == uid_box1)
    data_bb2 = next(item['bounding_box'] for item in berries if item["berry_uid"] == uid_box2)
    # box1 = x1, y1, x1+w1, y1+h1
    box1 = data_bb1['x'], data_bb1['y'], data_bb1['x'] + data_bb1['width'], data_bb1['y'] + data_bb1['height']
    # box2 = x2, y2, x2+w2, y2+h2
    box2 = data_bb2['x'], data_bb2['y'], data_bb2['x'] + data_bb2['width'], data_bb2['y'] + data_bb2['height']
    
    x_inter1 = max(box1[0],box2[0])
    y_inter1 = max(box1[1],box2[1])
    x_inter2 = min(box1[2],box2[2])
    y_inter2 = min(box1[3],box2[3])
    if x_inter2 - x_inter1 < 0 or y_inter2 - y_inter1 < 0 or (x_inter2 - x_inter1 < 0 and y_inter2 - y_inter1 < 0):
        return 0
    else:
        inter_width = abs(x_inter2 - x_inter1)
        inter_height = abs(y_inter2 - y_inter1)
        inter_area = inter_height * inter_width
        width_box1 = abs(box1[2]-box1[0])
        height_box1 = abs(box1[3]-box1[1])
        width_box2 = abs(box2[2]-box2[0])
        height_box2 = abs(box2[3]-box2[1])
        box1_area = width_box1 * height_box1
        box2_area = width_box2 * height_box2
        union_area = box1_area + box2_area - inter_area
        iou = inter_area/union_area
        return iou
    
# This function takes list of sorted berries based on euclidean distance as input
# Outputs: 1) List of unoccluded_berries in the given image 
#          2) List of occluded_berries in the given image 
# Since the list is already sorted based euclidean distance, this function takes advantage
# to give sorted unoccluded_berries and occluded_berries uids as two list.
def assort_berries(berries, list_uid):
    unoccluded_berries = []
    occluded_berries_sorted_euclidean = []
    for i in list_uid:
        occluded = False
        for j in list_uid:
            if i != j:
                if IoU(berries,i,j) != 0:
                    occluded = True
                    break
                else:
                    occluded = False
        if occluded:
            occluded_berries_sorted_euclidean.append(i)
        else:
            unoccluded_berries.append(i)
    return unoccluded_berries, occluded_berries_sorted_euclidean

# Since it depends on intrinsic and extrinsic properties of robotics arm, and current location of mobile robot.
# It is hard to compute reachability unless robot configuration is known.
def arm_can_reach(x: float, y: float, z: float) -> bool:
    """Whether the arm can reach a position (x, y, z)"""
    ...        

selected_berries = select_berry(candidates=berries)
print('Berries uids sorted based on euclidean distance :',selected_berries)
x,y = assort_berries(berries, selected_berries)
print('Unoccluded berries :',x)
print('Occluded berries :',y)