from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        task_content = request.form.get("task")
        if task_content:
            new_task = Task(content=task_content) #type:ignore pylance error for no parameter
            db.session.add(new_task)
            db.session.commit()

        return redirect(url_for("tasks"))

    all_tasks = Task.query.all()
    return render_template("tasks.html", tasks=all_tasks)

@app.route("/delete/<int:id>")
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()

    return redirect(url_for("tasks"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
