from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)


@app.route("/")
def index():
    return f"<a href = welcome.html>continue</a>"


@app.route("/welcome.html", methods = ["POST", "GET"])
def Welcome():
    if request.method == "POST":
        choice = request.form["options"]
        if choice == "password":
            return redirect("save_forget.html")
        elif choice == "hi":
            return redirect("meet.html")
        else:
            return f"<h1><center>You have to choose something...</center></h1>" \
                   f"<button><a href = 'welcome.html'>Go back</a></button>"

    else:
        return render_template("welcome.html")

@app.route("/save_forget.html", methods = ["POST", "GET"])
def choice():
    if request.method == "POST":
        password = request.form["password"]
        code_written = request.form["code"]
        code = random.randint(100000, 999999)
        password_dict = {}
        if password != "":
            if len(password) < 6:
                return f"<center><h1>Your password has to be at least 6 characters long.</h1><br>" \
                       f"<button><a href = 'save_forget.html'>Go Back</a></button></center>"
            elif len(password) > 5:
                if code in password_dict:
                    while code not in password_dict:
                        code = random.randint(100000,999999)
                        continue
                    password_dict[f"{code}"] = f"{password}"
                else:
                        password_dict[f"{code}"] = f"{password}"

        elif code != "":
            if len(code_written) < 6 or len(code_written) > 6:
                return f"<center><h1>Code has to be 6 didgets long.</h1><br>" \
                       "<button><a href = 'save_forget.html'>Go Back</a></button></center>"
            elif code_written not in password_dict:
                return f"<center><h1>This code does not exist</h1><br>" \
                       "<button><a href = 'save_forget.html'>Go Back</a></button></center>"

            elif code_written in password_dict:
                return f"<center><h1>Your password is {password_dict.get({code_written})}</h1><br>" \
                       "<button><a href = 'save_forget.html'>Go Back</a></button></center>"
        else:
            return f"<center><h1>Something went wrong!</h1><br>" \
                    "<button><a href = 'save_forget.html'>Try Again</a></button></center>"

    else:
        return render_template("save_forget.html")

@app.route("/meet.html", methods =  ["POST", "GET"])
def met():
        return render_template("meet.html")

if __name__ == '__main__':
    app.run()