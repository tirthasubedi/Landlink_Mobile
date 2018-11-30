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

    #return render_template("accountCreated.html")
    data = {}
    data['Email'] = request.form.get('Email')
    data['Password'] = request.form.get('Password')
    data['Name'] = request.form.get('Name')
    data['Address'] = request.form.get('Address')
    data['State'] = request.form.get('State')
    data['City'] = request.form.get('City')
    data['ZipCode'] = int(request.form.get('ZipCode'))
    data['Phone'] = int(request.form.get('Phone'))
    data['isFarmer'] = int(request.form.get('isFarmer'))

    query = "INSERT INTO `Applicants`(`Name`, `Email`, `Phone`, `Password`, `isFarmer`, `Address`, `State`, `City`, `ZipCode`, `ApplicantID`) VALUES ('{0}','{1}',{2},'{3}',{4},'{5}','{6}','{7}',{8},NULL)".format(data['Name'],data['Email'],data['Phone'],data['Password'],data['isFarmer'],data['Address'],data['State'],data['City'],data['ZipCode'])
    cur.execute(query)
    conn.commit()
    conn.close()    
    return render_template('accountCreated.html')

if __name__ == "__main__":
    app.run(debug = True)
