from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/", methods=['GET','POST']) #url to handle get and post reqs!!!
def index():
    # print(request.method)
    if request.method=='POST': #for submit button!!!
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        date=request.form['date']
        occupation=request.form['occupation']
        # print(first_name)

    return(render_template("index.html"))


app.run(debug=True,port=5001)

