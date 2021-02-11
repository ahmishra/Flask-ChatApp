from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/')
def home():
    return render_template("index.html")


@main.route('/enter-room', methods=['GET', 'POST'])
def enter_room():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('enter-chat-room.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.enter_room'))
    return render_template('chat.html', name=name, room=room)
