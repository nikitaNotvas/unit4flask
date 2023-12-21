from flask import Flask, render_template,request

app = Flask(__name__)

todolist=['Get to plat in overwatch 2 in tank or dps','Steal THE moon']



@app.route('/',methods=["GET","POST"])
def index():
    new_todo = request.form["new_todo"]
    todolist.append(new_todo)
    return render_template("todoweb.html.jinja",todolist=todolist)
    




