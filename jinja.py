###Building URL Dynamically
###Variable Rule
###Jinja2 Template Engine
from flask import Flask, render_template,request, redirect, url_for

### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask app </h1><html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index1.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html', results=res, score=score)  # Pass the score if needed
 

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={"score":score,"res":res}
    return render_template('result1.html',results=exp) 

@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html',results=score)    

@app.route("/fail/<int:score>")
def fail(score):
    res=""
    return render_template('result1.html',results=score)  
    
@app.route('/submit', methods=['POST','GET'])
def submit():
    # Extract scores from the form
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        # Calculate the average score
        total_score = (science + maths + c + data_science) / 4
    else :
        return render_template('geresults.html')
    # Redirect to the success page with the total score
    return redirect(url_for('successres', score=total_score))


if __name__ == "__main__":
    app.run(debug=True)