from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    
    return "hello djay"


@app.route('/api/')
def name(name):
     
    length = len(name)
    
    result = "hello " + name + "!"
    
    return result
    
if __name__ == '__main__' :

    app.run(debug=True)