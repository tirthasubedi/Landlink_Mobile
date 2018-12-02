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
    try:
    	data['ZipCode'] = int(request.form.get('ZipCode'))
    	data['Phone'] = int(request.form.get('Phone'))
    	data['isFarmer'] = int(request.form.get('isFarmer'))
    except:
	data['ZipCode'] = 0
	data['Phone']   = 0
	data['isFarmer'] = int(request.form.get('isFarmer'))

    query = "INSERT INTO `Applicants`(`Name`, `Email`, `Phone`, `Password`, `isFarmer`, `Address`, `State`, `City`, `ZipCode`, `ApplicantID`) VALUES ('{0}','{1}',{2},'{3}',{4},'{5}','{6}','{7}',{8},NULL)".format(data['Name'],data['Email'],data['Phone'],data['Password'],data['isFarmer'],data['Address'],data['State'],data['City'],data['ZipCode'])
    cur.execute(query)
    conn.commit()
    conn.close()
 
    #return render_template('accountCreated.html')
    if data['isFarmer']==1:
	return render_template('landOwnerSurvey.html')
    else:
	return render_template('landSeekerSurvey.html')

@app.route('/landOwnerSurvey',methods=['GET','POST'])
def landOwnerSurvey():
    return render_template('landOwnerSurvey.html')

@app.route('/landSeekerSurvey',methods=['GET','POST'])
def landSeekerSurvey():
    return render_template('landSeekerSurvey.html')

@app.route('/displayOwner' ,methods=['GET','POST'])
def dispOwner():
    fields = ['terms','other_desc','street','city','zip','region','acres','pasture',
    'tillable','woodland','housing_desc','goals','veg_hort','beef','dairy','poultry',
    'hogs','goats','sheep','horses','aqua','tobacco','row','rent_lease','purchase',
    'equipment_desc','irrigation']

    responses=[]

    for field in fields:
        if field in request.values.keys():
                if request.values[field] == 'on':
                        responses.append('1')
                else:
                        responses.append(str(request.values[field]))
        else:
                responses.append('0')

    formatFields="`owner_ID`, "+str(fields)[1:-1].replace("'","`")
    formatResponses="NULL, "+str(responses)[1:-1]
    query = "INSERT INTO `Landowners` ({0}) VALUES ({1});".format(formatFields,formatResponses)

    conn, cur = connect()
    cur.execute(query)
    conn.commit()
    conn.close()

    return render_template('accountCreated.html')


@app.route('/displaySeeker',methods=['GET','POST'])
def dispSeeker():

    fields = ['terms','amt_tillable','amt_pasture','organic','housing_desc','eq_storage','livestock_barn',
    'stables', 'greenhouse', 'desc_equip', 'irrigation', 'education', 'veg_horticulture',
    'cattle_beef', 'dairy', 'poultry', 'hogs', 'goats', 'sheep', 'horses', 'aqua', 'tobacco', 'row_crops',
    'rent_lease', 'purchase', 'location', 'goals', 'where_farming', 'how_sell']

    responses = []

    for field in fields:
	if field in request.values.keys():
		if request.values[field] == 'on':
			responses.append('1')
		else:
			responses.append(str(request.values[field]))
	else:
		responses.append('0')

    formatFields="`farmer_ID`, "+str(fields)[1:-1].replace("'","`")
    formatResponses="NULL, "+str(responses)[1:-1]
    query = "INSERT INTO `Farmers` ({0}) VALUES ({1});".format(formatFields,formatResponses)

    conn, cur = connect()
    cur.execute(query)
    conn.commit()
    conn.close()

    return render_template('accountCreated.html')

if __name__ == "__main__":
    app.run(debug = True)
