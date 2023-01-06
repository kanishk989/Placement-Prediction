import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
# Loading the model
model = pickle.load(open('templates/knn-model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Take the values from the user and use them to predict"""
    internships = int(request.form["internships"])
    cgpa = int(request.form["cgpa"])
    hostel = int(request.form["hostel"])
    backlogs = int(request.form["backlogs"])
    if cgpa < 6:
        output = 0
    elif internships > 1:
        output = 1
    elif backlogs > 2:
        output = 0
    else:
        prediction = model.predict([[internships, cgpa, hostel, backlogs]])
        output = prediction[0]
        
    return render_template('index.html', prediction_text=f'Chances of Placed in University placement drive is {output}')


if __name__ == "__main__":
    app.run()
