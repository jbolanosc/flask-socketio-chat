import json
from uuid import uuid4
from flask import Response, request, render_template, make_response, session, redirect, url_for
from util import user_join, create_room, get_all_rooms

def generate_routes(app):
    @app.route("/")
    def index():
        if 'username' in session:
            redirect(url_for('intro'), code=307)
        return make_response(render_template("index.html"))

    @app.route("/intro", methods=["POST"])
    def intro():
        rooms = get_all_rooms()
        if 'username' in session:
            username = request.form["username"]
            return make_response(render_template("intro.html", user=username, items=rooms ))
        elif 'username' in request.form:
            username = request.form["username"]
            session["username"] = username 
            return render_template("intro.html", user=username, items=rooms )
        
        return redirect(url_for('index'))

    @app.route("/chat", methods=["POST"])
    def chat():
        if 'newChannel' in request.form:
            new_id = str(uuid4())
            channel = request.form["newChannel"]
            username = session["username"]
            session["id"] = new_id
            room_id = create_room(channel)
            user = user_join(new_id, session["username"], room_id)
            json_user = json.dumps(user)
            return make_response(render_template("chat.html", user=json_user))

        elif 'channel' in request.form:
            new_id = str(uuid4())
            channel = request.form["channel"]
            username = session["username"]
            session["id"] = new_id
            user = user_join(new_id, session["username"], channel)
            json_user = json.dumps(user)
            return make_response(render_template("chat.html", user=json_user))
