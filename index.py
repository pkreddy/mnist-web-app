import base64
import io
from PIL import Image
from flask  import request
from flask import Flask, render_template
app = Flask(__name__)

def convert_and_save(b64_string):
    imgdata = base64.b64decode(b64_string.partition(",")[2])
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/img-data" , methods = ['POST'])
def imgdata():
    data = request.values
    if data is None:
        print("No data from the client")
        return jsonify({'error': 'Empty canvas!'})
    else:
        data = data['imgBase64']
        #data = data.replace('image/png','')
        convert_and_save(data)
        return "got the image thanks!"

if __name__ == "__main__":
    app.run(debug=True)