

from flask import Flask, request,jsonify,render_template
from flask_cors import CORS
import data_from_sql
import graph_data
app = Flask(__name__)
CORS(app)
@app.route('/')
def introduce():
    return render_template('traffic.html')

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

@app.route('/graph',methods = ['POST'])
def graph():
    result =  request.get_json(force = True)
    GuName = result['GuName']
    factor = result['factor']
    y = graph_data.return_graph_data(GuName,factor)
    return jsonify(y)

if __name__ == "__main__":
    app.run(debug=True)
# host = '0.0.0.0',port='5000'
