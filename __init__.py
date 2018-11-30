from flask import Flask, request, render_template
import MySQLdb

def connect():
    conn = MySQLdb.connect(db="cfa", host="localhost", user="cfa", passwd="kKGP4ylKt9n1UJac", port=3306)
    cur = conn.cursor()
    return conn, cur

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    conn, cur = connect()
    query = "SELECT * FROM Applicants"
    cur.execute(query)

    qResult = cur.fetchall()
    conn.close()
    return render_template("about.html",result=qResult)

@app.route('/sampleQuestion')
def sampleQuestion():
    return render_template("sampleQuestion.html")

@app.route('/forgotPassword')
def forgotPassword():
    return render_template("forgotPassword.html")

@app.route('/createAccount')
def createAccount():
    return render_template("createAccount.html")

@app.route('/confirmedSent')
def confirmedSent():
    return render_template("confirmedSent.html")

@app.route('/accountCreated',methods=['GET','POST'])
def accountCreated():
    conn,cur = connect()

    return render_template("accountCreated.html")
    #return request.form['Email']

if __name__ == "__main__":
    app.run(debug = True)
