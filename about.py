from app import *
from flask import render_template
from connect import connect

@app.route('/about')

def about():
    conn, cur = connect()
    query = "SELECT * FROM Applicants"
    cur.execute(query)

    qResult = cur.fetchall()
    conn.close()
    return render_template("about.html",result=qResult)
