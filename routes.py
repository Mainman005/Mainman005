from app import app,db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
#importing task class from models.py file
from models import Task
from datetime import datetime

import forms
@app.route('/')
@app.route('/index')
def index():

    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm() 
    if form.validate_on_submit():

        t = Task(title = form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task has been added to database')
        return redirect(url_for('index'))
        # return render_template('about.html', form=form, title=form.title.data)
    return render_template('add.html', form=form)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
# this a way to pass on some info to route function. the function edit now will have access to task id.
def edit(task_id):
    task = Task.query.get(task_id)
    # here the task id will give us the task that we are looking for.
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task has been edited.")
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash("Task not found")
    return redirect(url_for('index'))

## Before we change our current form title, we also want to see if thw form was submitted. Then we will update the task title. an update the task date, then we have to save it. since its alredy in data base so we dont need to add the task. we can commit the changes. and then we can flash a msg.then we will retuen and redirect to index page to see the changes. but if someonee doesnot submit the edit form then we will continue rendering the edit.html page.

# similar to edit functionality we need to write a route for the delete functionality. However we will need a new form for our delete page.

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
# this a way to pass on some info to route function. the function edit now will have access to task id.
def delete(task_id):
    task = Task.query.get(task_id)
    # here the task id will give us the task that we are looking for.
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task has been deleted.")
            return redirect(url_for('index'))

        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash("Task doesnot found")
    return redirect(url_for('index'))
    