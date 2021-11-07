from flask import Flask,render_template,redirect,request
from flask_app import app
# from flask_app.models.email import Emails
from flask_app.models.email import Emails

@app.route ("/")
def index():
    return render_template("index.html")

@app.route("/validate", methods=["POST"])
def validate_email():
    data = {
        "email":request.form["email"]
    }
    
    if Emails.validate_email(request.form):
        Emails.save(data)
        return redirect("/success")
    
    else:
        return redirect("/")

@app.route("/success")
def get_all():
    emails = Emails.get_all()
    return render_template("success.html", emails=emails)


@app.route("/delete/<int:id>")
def delete_user(id):
    data ={
        "id":id
    }
    Emails.delete_user(data)
    return redirect ("/success")