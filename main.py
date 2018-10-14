from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods =['POST', 'GET'])
def index_homepage():
    return render_template("index.html")

@app.route("/user_signup", methods=['POST'])
def user_signup():
    username = request.form['username']
    pswd = request.form['password']
    verify_pswd = request.form['verify_password']
    email= request.form['email']
    username_error = ''
    pswd_error = ''
    pswd_match_error = ''
    email_error = ''

    if (len(username) <3) or (len(username) >20) or (" " in username):
        username_error = "No space in username.  Please limit your characters to 3 or more characters up to 20."

    if (len(pswd) <3) or (len(pswd) >20) or (" " in pswd):
        pswd_error = "No space in password.  Please limit your characters to 3 or more characters up to 20."

    if (pswd != verify_pswd) or (verify_pswd == ""):
        pswd_match_error = "Please try again.  Passwords do not match."

    if (len(email) <3) or (len(email) >20) or (" " in email) and ("@" not in email) and ("." not in email):
        email_error = "No space in email allowed.  Please limit your characters to 3 or more characters up to 20."
        return render_template("index.html", username=username, email_error=email_error)

    if not (username_error) and not (pswd_error) and not (email_error) and not (pswd_match_error):
        return redirect (f"/welcome?username={username}")
    else:
        return render_template("index.html", username_error=username_error, pswd_error=pswd_error, pswd_match_error=pswd_match_error, email_error=email_error)

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

app.run()