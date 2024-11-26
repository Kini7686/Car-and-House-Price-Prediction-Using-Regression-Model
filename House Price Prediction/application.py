from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open('D:\Projects\AY21TECSM50115 Aditya Subhash Kini\AY21TECSM50115 Aditya Subhash Kini\House Price Prediction/LinearRegressionModelH.pkl','rb'))
car=pd.read_csv('D:\Projects\AY21TECSM50115 Aditya Subhash Kini\AY21TECSM50115 Aditya Subhash Kini\House Price Prediction/Mumbai1.csv')

# @app.route('/',methods=['GET','POST'])
# def index():
#     companies=sorted(car['company'].unique())
#     car_models=sorted(car['name'].unique())
#     year=sorted(car['year'].unique(),reverse=True)
#     fuel_type=car['fuel_type'].unique()

#     companies.insert(0,'Select Company')
#     return render_template('index.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    Location =request.form.get('Location')
    if (Location=='Kharghar'):
        Val1=0;
    elif(Location=='Thane West'):
        Val1=1;
    else:
        Val1=2;

    Area=request.form.get('Area')
    
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
    print(prediction)

    return str(np.round(prediction[0],2))



if __name__=='__main__':
    app.run()