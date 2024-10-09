from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
  return 'Homepage loaded'

@app.route('/home')
def home():
  return 'Hello World'

@app.route('/greet/<name>')
def greet(name):
  return f'Hello {name}'

@app.route('/add/<a>/<b>')
def add(a, b):
  result = int(a) + int(b)
  return render_template("index.html", result=result)
  # return f'Solution: {result}'

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
  if request.method == 'POST':
    num1 = request.form['num1']
    operation = request.form['operation']
    num2 = request.form['num2']

    if(operation == 'add'):
      return render_template("index.html", result = int(num1) + int(num2))
    elif(operation == 'subtract'):
      return render_template("index.html", result = int(num1) - int(num2)) 
    elif(operation == 'multiply'):
      return render_template("index.html", result = int(num1) * int(num2)) 
    elif(operation == 'divide'):
      if(int(num2) == 0):
        return render_template("index.html", result = 'Division by zero not possible.')
      return render_template("index.html", result = int(num1) / int(num2))
    else:
      return render_template("index.html", result = '') 

  elif request.method == 'GET':
    return render_template("index.html", result = '') 

products = [ {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10}, 
              {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 20}, 
              {"id": 3, "name": "Tablet", "price": 299.99, "stock": 15}
              ]

@app.route('/getProductInfo', methods=['GET'])
def getProductInfo():
  return products

@app.route('/getProductInfo/<id>', methods=['GET'])
def getProductInfoById(id):
  for p in products:
    if p['id'] == int(id):
      return p
  else:
    return 'No product found.'

@app.route('/addProduct', methods=['POST'])
def addProduct():
  # products.append(request.body)
  new_product = request.json
  item_available = False
  for item in products:
    if(item['id'] == new_product['id']):
      item_available = True
      break

  if(item_available == False):
    products.append(new_product)
  else:
    return jsonify('Product with same id already exists.')

  return jsonify('Product was successfully added.')

if __name__=='__main__':
  app.run(debug=True)
