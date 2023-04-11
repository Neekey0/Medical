from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def calculate():
    age = request.form['age']
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = request.form['children']
    smoker = request.form['smoker']
    region = request.form['region']
    
    model1 = pickle.load(open('model1.pkl','rb'))

    if sex == 'male':
        sex = 1
    else:
        sex = 0

    if smoker == 'yes':
        smoker = 0
    else:
        smoker = 1   

    if region == 'southeast':
        region = 0
    elif(region == 'southwest'):
        region = 1
    elif(region == 'northeast'):
        region = 2
    else:
        region =3   

    
    # pred = model1.predict([[31,0,25.74,0,1,0]])
    pred = model1.predict([[age,sex,bmi,children,smoker,region]])
    
    return render_template('index.html', pred = pred)

if __name__ == '__main__':
    app.run(debug=True)
