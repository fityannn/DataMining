from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Memuat model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    apotek = int(request.form['Apotek'])
    jan = int(request.form['Jan'])
    feb = int(request.form['Feb'])
    mar = int(request.form['Mar'])
    total = jan + feb + mar
    mean = int(total/3)

    # Membuat array fitur
    features = np.array([[apotek ,jan, feb, mar, total]])
        
    # Melakukan prediksi
    prediction = model.predict(features)
    Total = prediction[0]
    return render_template('index.html', Apotek=apotek, Jan=jan, Feb=feb, Mar=mar, Total=total, mean=mean)

if __name__ == '__main__':
    app.run(debug=True)
