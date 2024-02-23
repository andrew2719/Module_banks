# app.py

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    data_rate = float(data['dataRate'])
    message_size = float(data['messageSize'])
    medium_speed = float(data['mediumSpeed'])
    distance = float(data['distance'])

    transmission_delay = message_size / data_rate  # in seconds
    propagation_delay = distance / medium_speed  # in seconds

    return jsonify({
        'transmissionDelay': transmission_delay,
        'propagationDelay': propagation_delay
    })

if __name__ == '__main__':
    app.run(debug=True)
