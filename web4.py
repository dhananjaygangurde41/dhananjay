from flask import Flask ,request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    return render_template('index.html',day_of_week=day_of_week)


@app.route('/api')
def name():
     
    name = request.values.get('name')
    age = request.values.get('age')
    
    result = {
         'name' : name,
          'age' : age
    }
    return result
    
@app.route('/submit',methods=['POST'])
def submit():

    form_data = dict(request.form)
    
    print(form_data)
     
    return form_data
     
   # name = request.form.get('name')
  #  email = request.form.get('email')
    
    #return "hello, " + str(name) + ", " + str(email) + "!" 
    
if __name__ == '__main__' :

    app.run(host=0.0.0.0, debug=True)