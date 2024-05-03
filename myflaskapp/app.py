import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Database Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
DB_USER = 'root'
DB_PASSWORD = 'raman'
DB_NAME = 'raman'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@/'\
                          f'{DB_NAME}?host=34.172.193.238'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# Initialize Database
db = SQLAlchemy(app)
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class User(db.Model):
    __tablename__ = 'users'  # Changed table name to 'users' for clarity
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)  # Email is now optional

    def __repr__(self):
        return f'<User {self.username}>'


with app.app_context():
    db.create_all()

# ... imports




@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user_name = form.name.data
        try:
            existing_user = User.query.filter_by(username=user_name).first()
            if existing_user is None:
                new_user = User(username=user_name)
                db.session.add(new_user)
                db.session.commit()
                flash('Name successfully submitted.', 'success')
                form.name.data = ''  # Reset the form field
            else:
                flash('This name already exists.', 'error')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


# ... other routes


@app.route('/<name>')
def dire(name):
    return f'<h1>Hello, {name}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333