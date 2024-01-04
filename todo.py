from flask import Flask, render_template,request,redirect
import pymysql
import pymysql.cursors

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
    cursor=conn.cursor()

    cursor.execute("SELECT `description` FROM `todos` ")

    result = cursor.fetchall()
    
    for x in result:
        result=(x["description"])
    if request.method == "POST":
        new_todo = request.form["new_todo"]
        result.append(new_todo)

    return render_template("todoweb.html.jinja",todolist=result)

#@app.route('/delete_todo/<int:todo_index>',methods=["POST"])
#def todo_delete(todo_index):
#    
#    del todolist[todo_index]
#    return redirect('/')

