# Package importing
from flask import Flask, render_template, url_for, jsonify, request
import util

# Declaring the flasks app name
app = Flask(__name__)



# Default route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# favicon


@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='/images/favicon.png')

#  Get the location info.


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'location': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#  Get the parking info.
@app.route('/get_parking')
def get_parking():
    response = jsonify({'parking': util.get_parking()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#  Get the type of house info.
@app.route('/get_houseType')
def get_houseType():
    response = jsonify({'houseType': util.get_houseType()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#  Get the type of street info
@app.route('/get_streetType')
def get_streetType():
    response = jsonify({'streetType': util.get_streetType()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Route to predict the house prices

'''
this is our function, in which we take the inputs and give it to the trained model to process
and also to get the output
'''
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == "POST":
        # String datatype attributes
        location = request.form.get('ui-location')
        parking = request.form.get('ui-parking-facility')
        houseType = request.form.get('ui-house-type')
        streetType = request.form.get('ui-street-type')

        # int datatype attributes
        INT_SQFT = int(request.form.get('ui-int-sqft'))
        N_BEDROOM = int(request.form.get('ui-n-bedroom'))
        N_BATHROOM = int(request.form.get('ui-n-bathroom'))
        N_ROOM = int(request.form.get('ui-n-room'))
        QS_ROOMS = int(request.form.get('ui-qs-room'))
        QS_BATHROOM = int(request.form.get('ui-qs-bathroom'))
        QS_BEDROOM = int(request.form.get('ui-qs-bedroom'))
        QS_OVERALL = int(request.form.get('ui-qs-overall'))

        print('got the values in here!!!')
        #the below line is to load our trained model which is in the artifacts folder
        util.load_saved_artifacts()
        #the below line is to send all the inputs to the model and get the output from the model
        my_response = util.get_estimated_price(location, parking, houseType, streetType, INT_SQFT, N_BEDROOM, N_BATHROOM, N_ROOM, QS_ROOMS, QS_BATHROOM, QS_BEDROOM, QS_OVERALL)
        #the below line sends the output to the html file
        return render_template('index.html', response=my_response)


if __name__ == "__main__":
    app.run()
