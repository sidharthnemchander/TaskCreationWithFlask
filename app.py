from flask import Flask, request

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
    
    tasks_html = ""
    for t in tasks_list:
        tasks_html += f"<li>{t}</li>"

    return f"""
            <h2> NOT BAD FOR YOUR FIRST TIME </h2>
            
            <form method = "POST">
                <input type = "text" name = "task" placeholder = "Enter your task"/>
                <button type = "submit"> Add task </button>
            </form>

            <ul>
                {tasks_html}
            </ul>

            <a href = '/'> back </a>
            """

if __name__ == "__main__":
    app.run(debug = True)