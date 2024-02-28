from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from flask_cors import CORS
import base64
import random
app = Flask(__name__)
CORS(app)

class sever_find_blank:
    """docstring for sever_find_blank"""
    def __init__(self):
        pass
        
    def find_blank_area(self, img, stamp_width, stamp_height):
        # ค้นหาพื้นที่ว่างในรูปภาพ
        width, height = img.size
        # print(width,height)
        for x in range(0, width - stamp_width, random.choice(range(3,10))):
            print(x)
            for y in range(0, height - stamp_height + 1, 5):
               
                region = img.crop((x, y, x + stamp_width, y + stamp_height))
                region_data = list(region.getdata())
                # ตรวจสอบว่าพื้นที่นี้ว่างหรือไม่
                is_blank = all(pixel[2] == 255 for pixel in region_data)


                if is_blank:
                    # print("TEST in find blank")
                    return (x, y)
                
        # ถ้าไม่พบพื้นที่ว่าง
        return None

    def find_and_replace_blank(self, image_path, stamp):
        # โปรแกรมนี้ใช้ Pillow เพื่อประมวลผลรูปภาพ

        with Image.open(image_path) as img:

            for stamp_value in stamp.split(','):
                stamp_img = Image.open('./picture_stamp/'+stamp_value)

                width, height = stamp_img.size

                # ประมวลผลหาตำแหน่งที่จะใส่ stamp และทำการใส่ stamp
                # (โปรดปรับปรุงโค้ดตามความต้องการ)
                x = 0
                y = 0
                blank_area = self.find_blank_area(img, width, height)

                if blank_area is not None:
                    # ทำการใส่ stamp ลงไปในพื้นที่ว่าง
                    img.paste(stamp_img, blank_area, stamp_img)

        output_path = 'output_image.png'
        img.save(output_path)

        return output_path


   
