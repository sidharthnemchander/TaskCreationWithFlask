from flask import Flask, request, render_template

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

if __name__ == "__main__":
    app.run(debug = True)