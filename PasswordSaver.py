from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)


@app.route("/")
def index():
    return f"<a href = welcome.html>continue</a>"


@app.route("/welcome.html", methods = ["POST", "GET"])
def Welcome():
    if request.method == "POST":
        choice = request.form["password_saver"]
        if choice == "1":
            return redirect("save_forget.html")
        elif choice == "2":
            return redirect("meet.html")
        else:
            return f"<h1><center>You have to choose something...</center></h1>" \
                   f"<button><a href = 'welcome.html'>Go back</a></button>"

    else:
        return render_template("welcome.html")

@app.route("/save_forget.html", methods = ["POST", "GET"])
def choice():
    if request.method == "POST":
        decision = request.form["options"]
        if decision == "password":
            return redirect("password.html")

        elif decision == "code":
            return redirect("code.html")


        else:
            return render_template("something.html")

    else:
        return render_template("save_forget.html")


@app.route("/code.html", methods = ["POST", "GET"])
def code():
    if request.method == "POST":
        return render_template("code.html")
    else:
        return render_template("code.html")

passwords = []
codes = []

@app.route("/password.html", methods=["POST", "GET"])
def password():
        if request.method == "POST":
            passwd = request.form["password"]
            code = random.randint(100000, 999999)
            passwords.append(passwd)

            while len(codes) != len(codes) + 1:
                if code not in codes:
                    codes.append(code)
                else:
                    code = random.randint(100000, 999999)

            return f"<center><h1>Your code if you forget your password is {code}</h1></center>" \
                   f"<center><button><a href = 'password.html'>Go back</a></button></center>"
        else:
            return render_template("password.html")


@app.route("/meet.html", methods =  ["POST", "GET"])
def met():
        return render_template("meet.html")



if __name__ == '__main__':
    app.run()