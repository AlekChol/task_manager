from flask import Flask, render_template, request
from connection import database, session
from models import Base, Management

app=Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    title = 'Task_management'
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        category = request.form.get('category')
        status = request.form.get('status')
        print(f"Task Name: {task_name}, Category: {category}, Status: {status}")

        ''' 
        new_task = Management(task_name=task_name, category=category, status=status)
        session.add(new_task)
        session.commit()
        '''
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)









