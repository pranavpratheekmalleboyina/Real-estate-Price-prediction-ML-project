from flask import Flask,request,jsonify
app = Flask(__name__)
import logic

@app.route('/get_location_names')
def get_location_names():
    locations = logic.get_location_names()
    response = jsonify({"locations" : locations})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    location = request.form['location']
    sqft =  float(request.form['sqft'])
    bhk =  int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        "estimated price ": logic.get_estimated_price(location,sqft,bhk,bath)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    logic.load_artifact_names()
    app.run(port=5050,debug=True)