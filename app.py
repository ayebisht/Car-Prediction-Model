
from flask import *
import pickle
import sklearn

app=Flask(__name__)


def make_pred(inps):
    model = pickle.load(open('car_price_model.pkl','rb')) #unpickle
    res=model.predict([inps])[0]
    return res


@app.route("/")
def home_func():
    return render_template('home.html')


@app.route("/predlink",methods=['POST'])
def predict_func():
    wheels=int(request.form["wheels"])
    engine=int(request.form["engine"])
    width=int(request.form["width"])
    enginesize=int(request.form["enginesize"])
    horsepower=int(request.form["horsepower"])

    ip_params=[wheels,engine,width,enginesize,horsepower]

    result=make_pred(ip_params)
    return render_template("display.html",res=result)




if __name__=='__main__':
     app.run(debug=True)
