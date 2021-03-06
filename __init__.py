from flask import Flask, request, render_template, session
import MySQLdb


# Connection to the database
def connect():
    conn = MySQLdb.connect(db="cfa", host="localhost", user="cfa", passwd="kKGP4ylKt9n1UJac", port=3306)
    cur = conn.cursor()
    return conn, cur

app = Flask(__name__)

# The main login page
@app.route('/')
def index():
    return render_template("index.html")

# The CFA about page
@app.route('/about')
def about():
    conn, cur = connect()
    query = "SELECT * FROM Applicants"
    cur.execute(query)

    qResult = cur.fetchall()
    conn.close()
    return render_template("about.html",result=qResult)

# Verify the Login
@app.route('/logonVerify',methods=['GET','POST'])
def logonVerify():
    conn, cur = connect()
    query = "SELECT * FROM `Applicants` WHERE `Email`='{0}' and `Password`='{1}'".format(request.form.get('Email'),request.form.get('Password'))
    cur.execute(query)

    qResult = cur.fetchall()
    conn.close()

    if (cur.rowcount==0): # Run after failed login
	return index()+"<script>alert('Failed Login');</script>"
    
    page = ""
    page+='<table class="table table-striped">'
    for user in qResult:
	page+="<tr>"
	for item in user:
	    page=page+"<td>"+str(item)+"</td>"
	page=page+"</td>"

    page+="</table>"

    #return str(cur.rowcount)+" "+str(request.form.get('Email'))+" "+str(request.form.get('Password'))+" "+query
    return render_template("viewUser.html",result=qResult)

# A prototype sample question page for building additional forms
@app.route('/sampleQuestion')
def sampleQuestion():
    return render_template("sampleQuestion.html")

# A not-yet-implemented forgot password page
@app.route('/forgotPassword')
def forgotPassword():
    return render_template("forgotPassword.html")

# The Applicant creation page
@app.route('/createAccount')
def createAccount():
    return render_template("createAccount.html")

# Show the completed survey
@app.route('/confirmedSent')
def confirmedSent():
    return render_template("confirmedSent.html")

# Confirm account creation for applicant
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

# The Land Owner portion of the Survey
@app.route('/landOwnerSurvey',methods=['GET','POST'])
def landOwnerSurvey():
    return render_template('landOwnerSurvey.html')

# The land seeker portion of the survey
@app.route('/landSeekerSurvey',methods=['GET','POST'])
def landSeekerSurvey():
    return render_template('landSeekerSurvey.html')

# Display the Owners Data and send it to the database
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

#Display the Seeker information to the database
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

# Update data after login
@app.route('/updateData',methods=['GET','POST'])
def updateData():
    

    conn, cur = connect()

    return "Data Updated: "+request.values['item']+" to "+request.values['data']

if __name__ == "__main__":
    app.run(debug = True)
