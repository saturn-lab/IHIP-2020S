import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

bk_img = cv2.imread("报告模板.jpg")
#设置需要显示的字体
fontpath = "font/simsun.ttc"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
#绘制文字信息
draw.text((100, 300),  "姓名", font = font, fill = (255, 255, 255))
draw.text((100, 350),  "项目", font = font, fill = (255, 255, 255))
draw.text((100, 350),  "时长", font = font, fill = (255, 255, 255))
draw.text((100, 350),  "消耗卡路里", font = font, fill = (255, 255, 255))
draw.text((100, 350),  "动作标准数", font = font, fill = (255, 255, 255))
draw.text((100, 350),  "动作不标准", font = font, fill = (255, 255, 255))
bk_img = np.array(img_pil)

cv2.imshow("add_text",bk_img)
cv2.waitKey()
cv2.imwrite("add_text.jpg",bk_img)
