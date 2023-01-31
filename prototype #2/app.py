import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Rele Pin
rele = 4

#Status init of rele
releSts = 0

GPIO.setup(rele, GPIO.OUT)

GPIO.output(rele, GPIO.LOW)

@app.route("/")
def index():
    # Read Sensors Status
    releSts = GPIO.input(rele)
    templateData = {
        'title' : 'GPIO output Status!',
        'rele' : releSts,
    }
    return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'rele':
        actuator = rele

    if action == "on":
        GPIO.setup(actuator, GPIO.OUT)
    else :
        GPIO.setup(actuator, GPIO.IN)
        

    releSts = GPIO.input(rele)

    templateData = {
        'rele' : releSts,
    }
    return render_template('index.html', **templateData)
if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug=True)

