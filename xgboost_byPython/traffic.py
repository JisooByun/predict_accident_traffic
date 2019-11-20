

from flask import Flask, request,jsonify
from flask_cors import CORS
import data_from_sql
app = Flask(__name__)
CORS(app)
@app.route('/test',methods = ['POST'])
def hello():

    result =  request.get_json(force = True)
    GuName = result['GuName']
    factor = result['factor']
    value = result['value']
    print(GuName)
    print(factor)
    print(value)
    x = data_from_sql.return_top5_cross(GuName,factor,value)
    return jsonify(x)

if __name__ == "__main__":
    app.run(debug=True)
