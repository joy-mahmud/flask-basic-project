from flask import Flask,render_template,request,jsonify
import requests
app=Flask(__name__)

@app.route("/")
def home():
    name='habib'
    id=101
    languages=['javascript','php','rust','go']
    return render_template('home.html',name=name,id=id,lang=languages)

@app.route('/project/')
@app.route('/project/name')
def project():
    return "project flask"


@app.route("/user")
@app.route('/user/<name>')
def user(name="joy"):
    return f"hello {name}"

@app.route('/post/<int:postid>/<commentid>')
def post(postid,commentid):   
    return f"post:{postid} comment:{commentid}"

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username= request.form.get('username')
        password=request.form.get('password')
        
        return f"username:{username} password:{password}"
    else:
        return render_template('login.html')
@app.route('/api/countries')
def country():
    countries=['bangladesh','india','pakistan','australia','england']
    return jsonify({"countries":countries})

@app.route('/posts')
@app.route('/posts/<int:id>')
def posts(id=""):
    response=requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    return jsonify(response.json())

if __name__=="__main__":
    app.run(debug=True)