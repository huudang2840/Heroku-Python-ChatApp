from flask import Flask, render_template,request,flash,redirect,url_for,session, request
import sqlite3
import train
import chatapp

app = Flask(__name__)
app.secret_key="123"

con=sqlite3.connect("database.db")
con.execute("create table if not exists customer(pid integer primary key,name text,address text,contact integer,mail text)")
con.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        name=request.form['name']
        password=request.form['password']
     

        
        con=sqlite3.connect("database.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from customer where name=? and password=?",(name,password))
        data=cur.fetchone()

        if data:
            session["name"]=data["name"]
            session["password"]=data["password"]
            return redirect("customer")
        else:
            flash("Username and Password Mismatch","danger")
    return redirect(url_for("index"))


@app.route('/customer',methods=["GET","POST"])
def customer():
    train
    return render_template("dashboard.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            name=request.form['name']
            mail=request.form['mail']
            password = request.form['password']
            fullname=request.form['fullname']

            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("insert into customer(name,mail,password,fullname)values(?,?,?,?)",(name,mail,password,fullname))
            con.commit()
            flash("Record Added  Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("index"))
            con.close()

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/get")
def get_bot_response():
    chatapp
    userText = request.args.get('msg')
    return str(chatapp.chatbot_response(userText))


if __name__ == '__main__':
    app.run(debug=True)
