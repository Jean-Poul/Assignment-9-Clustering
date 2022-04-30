
# Import libraries
import numpy as np

# from sklearn.externals 
import joblib
import pickle
from flask import Flask, request, jsonify, render_template

# create an instance (our app)
app = Flask(__name__)
# app = Flask(__name__, template_folder='somefolder')

msmodel = joblib.load('msmodel.pkl')
pca = joblib.load('pca.pkl')

@app.route('/', methods=['GET', 'POST'])

@app.route('/hi/<name>')
def hello(name = None):
    return render_template('start.html', name=name)
# name is parameter in the template: {{name}}

@app.route('/predict')
def predict():
    return render_template('prediction.html')

@app.route('/predicted', methods=['GET', 'POST'])
def predicted():
    if request.method == 'POST':
        x1972 = request.form['x1']
        x1973 = request.form['x2']
        x1974 = request.form['x3']
        x1975 = request.form['x4']
        x1976 = request.form['x5']
        x1977 = request.form['x6']
        x1978 = request.form['x7']
        x1979 = request.form['x8']
        x1980 = request.form['x9']
        x1981 = request.form['x10']
        x1982 = request.form['x11']
        x1983 = request.form['x12']
        x1984 = request.form['x13']
        x1985 = request.form['x14']
        x1986 = request.form['x15']
        x1987 = request.form['x16']
        x1988 = request.form['x17']
        x1989 = request.form['x18']
        x1990 = request.form['x19']
        x1991 = request.form['x20']
        x1992 = request.form['x21']
        x1993 = request.form['x22']
        x1994 = request.form['x23']
        x1995 = request.form['x24']
        x1996 = request.form['x25']
        x1997 = request.form['x26']
        x1998 = request.form['x27']
        x1999 = request.form['x28']
        x2000 = request.form['x29']
        x2001 = request.form['x30']
        x2002 = request.form['x31']
        x2003 = request.form['x32']
        x2004 = request.form['x33']
        x2005 = request.form['x34']
        x2006 = request.form['x35']
        x2007 = request.form['x36']
        x2008 = request.form['x37']
        x2009 = request.form['x38']
        x2010 = request.form['x39']
        x2011 = request.form['x40']
        x2012 = request.form['x41']
        x2013 = request.form['x42']
        x2014 = request.form['x43']
        x2015 = request.form['x44']
        x2016 = request.form['x45']
        x2017 = request.form['x46']
        x2018 = request.form['x47']
        
        X = [[x1972, x1973, x1974, x1975, x1976, x1977, x1978, x1979, x1980, x1981, x1982, x1983, x1984, x1985, x1986, x1987, x1988, x1989, x1990, x1991, x1992, x1993,x1994, x1995, x1996, x1997, x1998, x1999, x2000, x2001, x2002, x2003, x2004, x2005, x2006, x2007, x2008,x2009, x2010, x2011, x2012, x2013, x2014, x2015, x2016, x2017, x2018]]
        newX = pca.transform(X)
        predicted = msmodel.predict(newX)
          
        return render_template("predicted.html", content=X, prediction=predicted)
    
@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run(debug=True)
