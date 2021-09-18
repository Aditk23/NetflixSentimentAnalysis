# Import libraries
#from types import MethodDescriptorType
from flask import Flask,render_template,request
import joblib

# create instance of an app
app = Flask(__name__)
tfidf = joblib.load('tfidf_vector_model.pkl')
model = joblib.load('netflix_model.pkl')
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/input',methods=['POST'])
def inputs():
    data = request.form.get('review')
    lst = []
    lst.append(data)
    vector = tfidf.transform(lst).toarray()
    prediction = model.predict(vector)
    if(prediction[0]==1):
        output = 'Positive Review'
    else:
        output='Negative Review'
    return render_template('output.html',predicted_text = pwdoutput)

@app.route('/again',methods=['POST'])
def again():
    return render_template('index.html')


# Run app
if __name__=='__main__':
    app.run(debug=True)