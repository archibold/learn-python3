from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def landing():
    ### send landing
    return """
        first you have to introduce yourself <br />
        go to /say_hello?username=yourname
        """

@app.route('/say_hello')
def say_hello():
    ### next step
    username = request.args.get('username', '')
    if not username:
        return "please introduce your self /say_hello?username=yourname"
    return """
    Hello {0}, if you want know what is going on near you<br />
    go to /get_info?long=<b>longitude</b>&lat=<b>latitude</b>
    """ .format(username)

@app.route('/get_info')
def get_info():
    ### search for message
    latitude = request.args.get('lat', '')
    longitude = request.args.get('long', '')
    return """
        <b>latitude: {0}</b> <b>longitude: {1}</b><br />
        nothing here, check other location
        """.format(latitude, longitude)

if __name__ == '__main__':
    app.run(debug=True)
