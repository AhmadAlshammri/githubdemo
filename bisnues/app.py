from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

# إعداد Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# إعداد Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# إنشاء النماذج (Models)
class Employee(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    approved = db.Column(db.Boolean, default=False)
    
class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    approved = db.Column(db.Boolean, default=False)
    
# تحميل المستخدم
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        employee = Employee.query.filter_by(email=email).first()
        
        if employee and employee.password == password and employee.approved:
            login_user(employee)
            return redirect(url_for('chat'))
        else:
            return "Invalid credentials or not approved by manager", 403
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/chat')
@login_required
def chat():
    if current_user.approved:
        return render_template('chat.html')
    return "Access Denied"

# تشغيل التطبيق
if __name__ == '__main__':
    db.create_all()  # إنشاء الجداول إذا لم تكن موجودة
    app.run(debug=True)
