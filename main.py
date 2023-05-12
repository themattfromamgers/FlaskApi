from flask import Flask, render_template,request, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

#request.get_json()

app = Flask(__name__)
cors = CORS(app)

client = MongoClient('mongodb+srv://burakyabgu:123@cluster0.8ciljw0.mongodb.net/?retryWrites=true&w=majority')
db = client['test']

@app.route('/')
def index():
    return render_template('adds.html')

@app.route('/hesapla', methods= ['GET', 'POST'])
def hesapla():
    if request.method == 'POST':
        number1 = request.form.get('number1')
        number2 = request.form.get('number2')
        print(f'{number1} {number2}')
        return redirect(url_for('index'))
    else:
        return "<h1>HATA</h1>"

@app.route('/data', methods = ['GET'])
@cross_origin()
def data():
    if(request.method == 'GET'):
        datalar = {
        "id": 1,
        "firstName":"Burak",
        "lastName": "Yabgu",
        "Age": 21
        }
  
        return jsonify(datalar)
@app.route('/mongo')
@cross_origin()
def pymongodeneme():
    # Verileri çekmek için bir koleksiyon seçin
    mycollection = db['todos']
    
    # Tüm verileri getirin
    result = mycollection.find()
    json_result = []
    for record in result:
        json_result.append({
            'id': str(record['_id']),
            'title': record['title'],
            'description': record['description']
        })
    return jsonify(json_result)
@app.route('/add', methods=['POST'])
def adds():

    data = request.get_json()
    mycollection = db['todos']
    

    result = mycollection.insert_one(data)
    print(result)
    print(data)
    return jsonify(data,)
if __name__ == "__main__":

    app.run(debug=True)