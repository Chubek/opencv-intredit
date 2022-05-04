from typing import Optional, Tuple

from pydantic import BaseModel


class Settings(BaseModel):
    """
    This object includes the settings for detection.

    Attributes
    ----------
    color_low: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]
        The low color threshold in HSV
    color_high: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]
        The high color threshold in HSV
    red_thresh: Optional[int]
        The supposed threshold to filter color after reds are filtered
    dp: Optional[float]
        Circle detection; inverse ratio of the accumulator resolution to the image resolution
    min_dist_circle: Optional[int]
        Circle detection; minimum distance of circles from one another
    min_radius: Optional[int]
        Circle detection; minimum radius of the supposed circles
    max_radius: Optional[int]
        Circle detection; maximum radius of the supposed circles
    param_1: Optional[int]
        The first parameter for HOUGH_CIRCLES_GRADIENT method; the higher threshold of the two passed to the Canny edge detector
    param_2: Optional[int]
        The second parameter for HOUGH_CIRCLES_GRADIENT method; he accumulator threshold for the circle centers at the detection stage
    thresh_temp: Optional[float] 
        The SSIM threshold with wihch the detected circles should be to the target signs
    do_op: Optional[bool]
        Whether to do opening, closing, blurring etc operations on image upon color isolation (prefrably on)
    """
    color_low: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = (
        (120, 50, 50), (130, 255, 255))
    color_high: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = (
        (150, 60, 50), (180, 255, 255))
    red_thresh: Optional[int] = 120
    dp: Optional[float] = 2.8
    min_dist_circle: Optional[int] = 400
    min_radius: Optional[int] = 2
    max_radius: Optional[int] = 250
    param_1: Optional[int] = 400
    param_2: Optional[int] = 120
    thresh_temp: Optional[float] = 0.85
    do_op: Optional[bool] = True
    do_op_hsv: Optional[bool] = True
    do_op_circle: Optional[bool] = True
    add_hue: Optional[int] = 20
    do_classify: Optional[bool] = True