from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open('D:\Projects\AY21TECSM50115 Aditya Subhash Kini\AY21TECSM50115 Aditya Subhash Kini\House Price Prediction/LinearRegressionModelH.pkl', 'rb'))
house_csv = pd.read_csv('D:\Projects\AY21TECSM50115 Aditya Subhash Kini\AY21TECSM50115 Aditya Subhash Kini\House Price Prediction/Mumbai1.csv')

@app.route('/')
def hello_world():
    return render_template('house.html')

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    Area=request.form.get('Area')
    Location =request.form.get('Location')
    if (Location=='Kharghar'):
        Val1=0;
    elif(Location=='Thane West'):
        Val1=1;
    else:
        Val1=2;

    
    Bedrooms=request.form.get('Bedrooms')
    if(Bedrooms=="1"):
        Val2=1;
    elif(Bedrooms=="2"):
        Val2=2;
    else:
        Val2=3;
    NR=request.form.get('NR')
    if(NR=='N'):
        Val3=0;
    else:
        Val3=1;
# lin_reg_model.predict(pd.DataFrame([[681,2,1,0]],columns=['Area','Location','Bedrooms','New_Resale']))
    prediction=model.predict(pd.DataFrame([[Area,Val1,Val2,Val3]],columns=['Area','Location','Bedrroms','New_Resale']))
    
    # print(prediction)

    return str(int(prediction[0]))

    # return render_template(house.html , prediction=prediction)
    # return str(np.round(prediction[0],2))



if __name__=='__main__':
    app.run(debug=True)