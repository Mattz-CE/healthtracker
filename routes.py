from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_title = request.form['title']
#         task_content = request.form['content']
#         new_task = Todo(title=task_title, content=task_content)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'
#         return 's'
#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         render = render_template('index.html', tasks=tasks)
#         return render

@app.route('/', methods=['POST', 'GET'])
def index():
    # redirect to login page
    return redirect('/signin')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('upda\watchte.html', task=task)


@app.route('/signin')
def signin():
    return render_template('signin.html')
