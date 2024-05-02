import cv2
import variable
from PIL import ImageFont, ImageDraw, Image
import numpy as np

box_loc = [400, 380]    #박스의 중심점

def draw_box(frame):
    global box_loc
    variable.square_center_x, variable.square_center_y = box_loc[0], box_loc[1]
    square_length_x = 260
    square_length_y = 420
    start_x = variable.square_center_x - square_length_x // 2
    start_y = variable.square_center_y - square_length_y // 2
    end_x = start_x + square_length_x
    end_y = start_y + square_length_y

    square_color = (0, 0, 0)
    square_thickness = 1
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), square_color, square_thickness)

    mid_x = start_x + square_length_x // 2
    cv2.line(frame, (mid_x, start_y), (mid_x, variable.square_center_y), square_color, square_thickness)

    mid_y = start_y + square_length_y // 2
    cv2.line(frame, (start_x, mid_y), (end_x, mid_y), square_color, square_thickness)

def draw_hangul_text(image, text, position, font_path, font_size, color):
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=color)
    return cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
