from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hi.html")


@app.route("/welcome.html", methods = ["POST", "GET"])
def Welcome():
    if request.method == "POST":
        choice = request.form["password_saver"]
        if choice == "meet":
            return redirect("save.html")
        elif choice == "forget":
            return redirect("forget.html")
        elif choice == "meet":
            return redirect("meet.html")
        else:
            return ("something.html")
    else:
        return render_template("welcome.html")

@app.route("/forget.html", methods = ["POST", "GET"])
def forgotten():
    print("hi")

@app.route("/save.html", methods = ["POST", "GET"])
def saved():
    print("hi")

@app.route("/meet.html", methods =  ["POST", "GET"])
def met():
    if request.method == "POST":
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    else:
        render_template("meet.html")

def save_to_database(password):
    sql = f"INSERT INTO passwordTable(passwords) VALUES('{password}' , ID_PASSWORD int PRIMARY_KEY AUTO_INCREMENT);"
    print(sql)
    connectionCreated = create_connection()
    insert_to_database(sql, connectionCreated)

def create_connection():
    print("Connection to database")
    connection = mysql.connector.connect(
        user="password.saver",
        password="cth2LtgDVX",
        host="37.59.55.185",
        port="3306",
        database="passwordTable"
    )
    print(connection)
    return connection

def insert_to_database(sql, connection):
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run()