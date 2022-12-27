import flask
import OPi.GPIO as GPIO
import os
app = flask.Flask(__name__)

#GPIO.setboard()
PORT = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT, GPIO.OUT)

@app.route("/")
def hello_world():
    return flask.render_template('index.html')
    
@app.route("/on",methods=["POST"])
def test():
    GPIO.output(PORT, GPIO.LOW)
    print('on')
    return flask.redirect('/')

@app.route("/off",methods=["POST"])
def test1():
    GPIO.output(PORT, GPIO.HIGH)
    #GPIO.cleanup()
    print('off')
    return flask.redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
