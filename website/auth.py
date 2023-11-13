from flask import Blueprint, render_template, flash, redirect, request, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

"""
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
        else:
            flash('Email does not exits.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
"""
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email ja existe', category='error')
        elif len(email) < 4:
            flash('Email precisa ser maior que 3 caracteres', category='error')
        elif len(first_name) < 2:
            flash('Nome precisa ser maior que 1 caractere', category='error')
        else:
            new_user = User(email=email, first_name=first_name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Conta Criada!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)