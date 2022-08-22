import json

from flask import Flask, request, jsonify,url_for,render_template
import util
from main import Prediction

app = Flask(__name__, template_folder='template')

with open('static/categories.json', 'r', encoding='utf8') as f:
    categories=json.load(f)

@app.route('/')
def home():
    return render_template('index.html',warming_type=categories['warming_type'],credit_eligible=categories['credit_eligible'],floor_location=categories['floor_location'],district=categories['district'])

@app.route('/get_features', methods=['GET'])
def get_features():
    response = jsonify({
        'district': util.get_district_names(),
        'warming_type': util.get_warming_type_names(),
        'credit_eligible': util.get_credit_eligible_names(),
        'floor_location': util.get_floor_location_names(),
    })

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    number_of_rooms = request.form['number_of_rooms']
    m2 = request.form['m2']
    building_age = request.form['building_age']
    bath_number = request.form['bath_number']
    warming_type = request.form['warming_type']
    credit_eligible = request.form['credit_eligible']
    floor_location = request.form['floor_location']
    district = request.form['district']
    data = {
        'estimated_price': Prediction().predict(number_of_rooms, m2, building_age, bath_number, warming_type,
                                                credit_eligible, floor_location, district)
    }

    return render_template('index.html', data=int(data['estimated_price']),warming_type=categories['warming_type'],credit_eligible=categories['credit_eligible'],floor_location=categories['floor_location'],district=categories['district'])


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
