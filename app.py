from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    name='habib'
    id=101
    return render_template('home.html',name=name,id=id)

@app.route("/user")
@app.route('/user/<name>')
def user(name="joy"):
    return f"hello {name}"

@app.route('/post/<int:postid>/<commentid>')
def post(postid,commentid):   
    return f"post:{postid} comment:{commentid}"

if __name__=="__main__":
    app.run(debug=True)