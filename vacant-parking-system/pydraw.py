import cv2 as open_cv
from line_colors import COLOR_RED

# drawing lines on to image
def draw_line(image,
                  coordinates,
                  label,
                  font_color,
                  border_color=COLOR_RED,
                  line_thickness=1,
                  font=open_cv.FONT_HERSHEY_SIMPLEX,
                  font_scale=0.5):
    open_cv.drawContours(image,
                         [coordinates],
                         contourIdx=-1,
                         color=border_color,
                         thickness=2,
                         lineType=open_cv.LINE_8)
    cordin = open_cv.moments(coordinates)

    center = (int(cordin["m10"] / cordin["m00"]) - 3,
              int(cordin["m01"] / cordin["m00"]) + 3)

    open_cv.putText(image,
                    label,
                    center,
                    font,
                    font_scale,
                    font_color,
                    line_thickness,
                    open_cv.LINE_AA)
