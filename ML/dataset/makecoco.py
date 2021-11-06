import os
import json
from PIL import Image

path = "./annos"
file_list = os.listdir(path)
# print(len(file_list))
file_name = 1
# print("{0:06d}".format(file_name))

for file in file_list:
    file_number = file[0:6]
    print(file_number)
    with open("annos/" + file, "r") as st_json:
        st_python = json.load(st_json)
        f = open("coco/" + file_number + ".txt", "w")
        image = Image.open("image/" + file_number + ".jpg")
        img_width = image.size[0]
        img_height = image.size[1]
        i = 0
        flag = 0
        while i < 20:
            item = "item" + str(i)
            if item in st_python:
                # print(st_python[item]["bounding_box"])
                data_class = st_python[item]["category_id"]
                # print(data_class)
                x1 = st_python[item]["bounding_box"][0]
                y1 = st_python[item]["bounding_box"][1]
                x2 = st_python[item]["bounding_box"][2]
                y2 = st_python[item]["bounding_box"][3]
                data_x_center = (x1 + x2) / 2
                data_y_center = (y1 + y2) / 2
                data_x_width = x2 - x1
                data_y_width = y2 - y1
                mod_x_center = data_x_center / img_width
                mod_x_center = round(mod_x_center, 6)
                mod_y_center = data_y_center / img_height
                mod_y_center = round(mod_y_center, 6)
                mod_x_width = data_x_width / img_width
                mod_x_width = round(mod_x_width, 6)
                mod_y_width = data_x_width / img_height
                mod_y_width = round(mod_y_width, 6)
                result = (
                    str(data_class)
                    + " "
                    + str(mod_x_center)
                    + " "
                    + str(mod_y_center)
                    + " "
                    + str(mod_x_width)
                    + " "
                    + str(mod_y_width)
                    + "\n"
                )
                f.write(result)
            else:
                flag += 1
                pass
            if flag == 2:
                break

            i += 1
