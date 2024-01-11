from flask import Flask, render_template,request,redirect
import pymysql,pymysql.cursors
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()
app = Flask(__name__)


conn = pymysql.connect(
    database="nvasiuta_todos",
    user="nvasiuta",
    password="244805859",
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)


users = {
    "humano": generate_password_hash ("no")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/',methods=["GET","POST"])
@auth.login_required
def index():

    if request.method == "POST":
        new_todo = request.form["new_todo"]
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (description) VALUES ('{new_todo}')")
        cursor.close()
        conn.commit()

    cursor=conn.cursor()

    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")

    result = cursor.fetchall()
    
    cursor.close()
    conn.commit()




    return render_template("todoweb.html.jinja",todolist=result)

@app.route('/delete_todo/<int:todo_index>',methods=["POST"])
def todo_delete(todo_index):
    
    cursor=conn.cursor()

    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")

    cursor.close()
    conn.commit()
    return redirect('/')

@app.route('/complete_todo/<int:todo_index>',methods=["POST"])
def todo_markcom(todo_index):
    
    cursor=conn.cursor()

    cursor.execute(f"UPDATE `todos` SET `complete`= 1 WHERE `id` = {todo_index} ")

    cursor.close()
    conn.commit()
    return redirect('/')

@app.route('/uncomplete_todo/<int:todo_index>',methods=["POST"])
def todo_unmarkcom(todo_index):
    
    cursor=conn.cursor()

    cursor.execute(f"UPDATE `todos` SET `complete`= 0 WHERE `id` = {todo_index} ")

    cursor.close()
    conn.commit()
    return redirect('/')