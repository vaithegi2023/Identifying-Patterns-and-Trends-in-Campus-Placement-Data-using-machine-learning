from flask import Flask,render_template,request
app=Flask(__name__, static_folder='static')
import pickle
model=pickle.load(open("placement.pkl",'rb'))

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/guest')
def guest():

	return render_template("index1.html")


@app.route('/y_predict',methods=["POST"])
def y_predict():

	sen1=request.form["sen1"]
	sen2=request.form["sen2"]
	sen3=request.form["sen3"]
	sen4=request.form["sen4"]
	sen5=request.form["sen5"]
	sen6=request.form["sen6"]
	value=[[int(sen1),int(sen2),int(sen3),int(sen4),int(sen5),int(sen6)]]
	#x_test=[[(yo) for yo in request.form.values()]]
	prediction=model.predict(value)
	prediction=prediction[0]
	if  prediction==1:
		return  render_template("secondpage.html")
	else:
		return render_template("secondpage2.html")
if __name__=='__main__':
	app.run(debug=True)