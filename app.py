from flask import Flask, request, render_template, request, url_for, redirect

app = Flask(__name__)

tasks_list = []

@app.route("/")
def home():
    return """
            <h1> this is the heading </h1>
            <p> how are you doing dude </p>
            <a href= '/tasks'> click this to go to tasks page <a>
            """

@app.route("/tasks", methods = ["GET", "POST"])
def tasks():
    if request.method == "POST":
        task = request.form.get("task")

        if task:
            tasks_list.append(task)
    
    return render_template("tasks.html", tasks=tasks_list)


@app.route("/delete/<int:index>")
def delete_task(index):
    if 0<=index < len(tasks_list):
        tasks_list.pop(index)
    return redirect(url_for("tasks"))

if __name__ == "__main__":
    app.run(debug = True)