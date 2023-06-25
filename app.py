import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle


app=Flask(__name__, template_folder='templates')
model=pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')
    
    
@app.route('/predict',methods=['POST'])
def predict():
    init_features=[int(x) for x in request.form.values()]   # it takes values from text field 
    final_features=[np.array(init_features)]
    print(final_features)
    prediction=model.predict(final_features)
    print(prediction)
    output=round(prediction[0],2)
    
    return render_template('index.html',prediction_text='Employee sakary should be ${}'.format(output))   #  prediction text gets replaced with prediction text in index.html
    
if __name__=="__main__":
    app.run(debug=True)
