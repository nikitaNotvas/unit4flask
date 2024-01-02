from flask import Flask, render_template,request,redirect

app = Flask(__name__)

todolist=['Get to plat in overwatch 2 in tank or dps','Steal THE moon']



@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"]
        todolist.append(new_todo)

    return render_template("todoweb.html.jinja",todolist=todolist)
    
@app.route('/delete_todo/<int:todo_index>',methods=["POST"])
def todo_delete(todo_index):
    
    del todolist[todo_index]
    return redirect('/')

