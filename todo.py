from flask import Flask, render_template,request,redirect
import pymysql,pymysql.cursors


conn = pymysql.connect(
    database="nvasiuta_todos",
    user="nvasiuta",
    password="244805859",
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)




app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():

    if request.method == "POST":
        new_todo = request.form["new_todo"]
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (description) VALUES ('{new_todo}')")
        cursor.close()
        conn.commit()

    cursor=conn.cursor()

    cursor.execute("SELECT * FROM `todos` ")

    result = cursor.fetchall()
    
    cursor.close()




    return render_template("todoweb.html.jinja",todolist=result)

@app.route('/delete_todo/<int:todo_index>',methods=["POST"])
def todo_delete(todo_index):
    
    cursor=conn.cursor()

    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")

    cursor.close()
    return redirect('/')

