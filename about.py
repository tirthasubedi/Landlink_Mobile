from app import *

@app.route('/about', methods=['POST','GET']) # Allow POST operations
def about():
    return render_template("about.html")
