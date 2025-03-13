from flask import Flask, render_template, jsonify, request
from PIL import Image

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getImages', methods=['POST'])
def getImages():
    numImg = request.json.get('numberImg')
    img_path = r"\\PRINTSERVER1\CapImages"
    png_img_path = os.path.join(img_path, f'img{numImg}.png')

    print(png_img_path)
    if not os.path.exists(png_img_path):
        return jsonify({'result': 'error'})

    # Mở tệp ảnh đối tượng
    obj = Image.open(png_img_path).convert("RGBA")
    # Mở tệp ảnh nền cabin (ảnh nhỏ)
    # w 2008 / h 2008
    resized_dimensions = (int(3008 * 0.6), int(2008 * 0.6))

    obj_cc = obj.resize(resized_dimensions)  # in case

    objcc_alpha = obj_cc.split()[3]
    back_cabin = Image.open("static/background/back_cabin.png").convert("RGBA")
    front_cabin = Image.open("static/background/front_cabin.png").convert("RGBA")
    front_cabin_alpha = front_cabin.split()[3]

    # Chỉnh vị trí của đối tượng trên ảnh cabin
    x_position = 1020  # horizontal_ left
    y_position = 180  # vertical_ upper
    back_cabin.paste(obj_cc, (x_position, y_position), objcc_alpha)
    back_cabin.paste(front_cabin, (0, 0), front_cabin_alpha)
    # back_cabin.show()

    # Mở tệp ảnh các nền khác
    obj_other_alpha = obj.split()[3]

    bg1 = Image.open("static/background/BKG2.jpg").convert("RGBA")
    bg2 = Image.open("static/background/BKG3.jpg").convert("RGBA")
    bg3 = Image.open("static/background/BKG4.jpg").convert("RGBA")

    # Chỉnh vị trí của đối tượng trên các nền khác
    x_position_other_bg = 400  # horizontal position
    y_position_other_bg = 250  # vertical position

    bg1.paste(obj, (x_position_other_bg, y_position_other_bg), obj_other_alpha)
    bg2.paste(obj, (x_position_other_bg, y_position_other_bg), obj_other_alpha)
    bg3.paste(obj, (x_position_other_bg, y_position_other_bg), obj_other_alpha)

    # Lưu các hình ảnh đã tạo ra

    path_folder = f'static\\images\\{numImg}'

    if not os.path.exists(path_folder):
        os.makedirs(path_folder)

    # Lưu hình ảnh vào thư mục /images
    path_bg1 = os.path.join(path_folder, f'{numImg}_bg1.png')  # Đặt đường dẫn lưu tệp
    path_bg2 = os.path.join(path_folder, f'{numImg}_bg2.png')
    path_bg3 = os.path.join(path_folder, f'{numImg}_bg3.png')
    path_bg4 = os.path.join(path_folder, f'{numImg}_bg4.png')

    # Lưu hình ảnh vào tệp
    back_cabin.save(path_bg1)
    bg1.save(path_bg2)
    bg2.save(path_bg3)
    bg3.save(path_bg4)

    return jsonify({'background1': path_bg1, 'background2': path_bg2, 'background3': path_bg3, 'background4': path_bg4})

if __name__ == '__main__':
    app.run(debug=True)