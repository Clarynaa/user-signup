from flask import Flask, request, render_template, redirect, logging

app = Flask(__name__)
app.config['DEBUG'] = True

u_err=""
pw_err=""
pwc_err=""
e_err=""

def u_valid(username):
    global u_err
    if " " in username:
        u_err = "Username cannot contain a space"
        return False
    else:
        if 2 < len(username) < 21:
            u_err = ""
            return True 
        else:
            u_err = "Username must be between 3 and 20 characters"
            return False

def p_valid(pw):
    global pw_err
    if " " in pw:
        pw_err = "Password cannot contain a space"
        return False
    else:
        if 2 < len(pw) < 21:
            pw_err = ""
            return True 
        else:
            pw_err = "Password must be between 3 and 20 characters"
            return False

def p_match(pw, pwc):
    global pw_err
    global pwc_err
    if pw == pwc:
        return True
    else:
        pw_err = "Passwords do not match"
        pwc_err = "Passwords do not match"
        return False

def e_exist(email):
    if len(email) > 0:
        return True
    else:
        return False

def e_valid(email):
    global e_err
    if " " in email:
        e_err = "Email cannot contain a space"
        return False
    elif email.count("@") != 1:
        e_err = "Email must contain exactly one @"
        return False
    elif email.count(".") != 1:
        e_err = "Email must contain a period"
    else:
        return True


@app.route("/")
def index():
    return render_template("signup.html", title="Signup", user_error=u_err, pw_error=pw_err, pwc_error=pwc_err, email_error=e_err)

@app.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    passwordc = request.form['passwordc']
    email = request.form['email']
    if u_valid(username) and p_valid(password) and p_match(password, passwordc):
        if not e_exist(email):
            return render_template("welcome.html", title="Welcome", username=username, email=email, user_error=u_err, pw_error=pw_err, pwc_error=pwc_err, email_error=e_err)
        elif e_valid(email):
            return render_template("welcome.html", title="Welcome", username=username, email=email, user_error=u_err, pw_error=pw_err, pwc_error=pwc_err, email_error=e_err)
        else:
             return render_template("signup.html", title="Signup", username=username, email=email, user_error=u_err, pw_error=pw_err, pwc_error=pwc_err, email_error=e_err)
    else:
         return render_template("signup.html", title="Signup", username=username, email=email, user_error=u_err, pw_error=pw_err, pwc_error=pwc_err, email_error=e_err)


app.run()