from flask import Flask,render_template,request
import requests  

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp',methods=['POST' , 'GET'])
def get_weatherdata():
    apikey='79d5d637a49392c4d93b6486c022c6f5'
    url='https://api.openweathermap.org/data/2.5/weather'

    params ={'q':request.form.get("city"),
         'appid':apikey,
         'units':request.form.get("units")
         }
    response=requests.get(url,params=params)
    data=response.json()
    return f"data : {data}"


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5002)