from flask import Flask, g, request
from flask import render_template, url_for, redirect
from application import app
from models import User
from forms import LoginForm

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if hasattr(g, "user") and  g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        # login and validate the user...
        user = db.session.query(User).filter(User.username == form.username).first()
        if user is None:
            flash("User does not exist or password is incorrect")
        else:
            phash = hashlib.sha256(form.password+user.salt)
            if phash == user.password:
                login_user(user)
                flash("Logged in successfully.")
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash("User does not exist or password is incorrect")

    return render_template("login.html", form = form)
