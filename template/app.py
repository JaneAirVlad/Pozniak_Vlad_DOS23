# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def user_list():
    # Список пользователей
    users = [
        {'name': 'Иван Иванов', 'email': 'ivan@example.com'},
        {'name': 'Петр Петров', 'email': 'petr@example.com'},
        {'name': 'Сидор Сидоров', 'email': 'sidor@example.com'}
    ]
    return render_template('template.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
