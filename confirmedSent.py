from app import *

@app.route('/confirmedSent')
def confirmedSent():
    return render_template("confirmedSent.html")
