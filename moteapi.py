from colorsys import hsv_to_rgb, rgb_to_hsv
from mote import Mote
from flask import Flask, jsonify, make_response

app = Flask(__name__)
mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

colour = 'FFFFFF'
status = 0

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    return tuple(int(value[i:i + length / 3], 16) for i in range(0, length, length / 3))

def mote_on(c):
    r, g, b = hex_to_rgb(c)
    for channel in range(4):
        for pixel in range(16):
            mote.set_pixel(channel + 1, pixel, r, g, b)
    mote.show()
    return True

def mote_off():
    mote.clear()
    mote.show()
    return True

def get_status():
    global status
    for channel in range(4):
        for pixel in range(16):
            if mote.get_pixel(channel + 1, pixel) != (0, 0, 0):
                status = 1
    return status

@app.route('/mote/api/v1.0/<string:st>', methods=['GET'])
def set_status(st):
    global status, colour
    if st == 'on':
        status = 1
        mote_on(colour)
    elif st == 'off':
        status = 0
        mote_off()
    elif st == 'status':
        status = get_status()
    return jsonify({'status': status, 'colour': colour})

@app.route('/mote/api/v1.0/set', methods=['GET'])
def get_colour():
    global colour
    return jsonify({'status': status, 'colour': colour})

@app.route('/mote/api/v1.0/set/<string:c>', methods=['GET'])
def set_colour(c):
    global status, colour
    colour = c
    if status != 0:
        mote_on(colour)
        status = 1
    return jsonify({'status': status, 'colour': colour})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    mote_off()
    app.run(host='0.0.0.0', debug=True)
