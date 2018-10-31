from app import *

@app.route('/sampleQuestion')
def sampleQuestion():
    return render_template("sampleQuestion.html")
