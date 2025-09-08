from flask import Flask ,request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/api')
def name():
     
    name = request.values.get('name')
    age = request.values.get('email')
    
    result = {
         'name' : name,
          'age' : email
    }
    return result
    
if __name__ == '__main__' :

    app.run(debug=True)