from flask import Flask, send_file
import os
import random

app = Flask(__name__)

image_directory = 'images'  # Папка с изображениями

@app.route('/random-image')
def random_image():
    image_files = os.listdir(image_directory)
    random_image_filename = random.choice(image_files)
    image_path = os.path.join(image_directory, random_image_filename)
    return send_file(image_path, mimetype='image/jpeg')  # Измените mimetype в зависимости от типа ваших изображений

if __name__ == '__main__':
    app.run(debug=True)
