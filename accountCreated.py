from app import *

@app.route('/accountCreated')
def accountCreated():
    return render_template("accountCreated.html")
