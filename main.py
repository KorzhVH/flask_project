from flask import Flask

app = Flask(__name__)


@app.route("/vacancy/")
def vacancy():
    return 'any vacancy'


@app.route("/vacancy/id/")
def vacancy_id():
    return 'vacancy by id'


@app.route("/vacancy/id/events/")
def vacancy_events():
    return 'show all events'


@app.route("/vacancy/id/events/event_id/")
def show_event_by_id():
    return 'show event by id'


@app.route("/vacancy/id/history/")
def vacancy_history():
    return 'any vacancy'


@app.route("/user/")
def get_user_main_page():
    return 'any vacancy'


@app.route("/user/calendar/")
def user_calendar():
    return 'show user calendar'


@app.route("/user/mail/")
def user_mail():
    return 'show users mail box '


@app.route("/user/settings/")
def user_settings():
    return 'any vacancy'


@app.route("/user/documents/")
def user_documents():
    return 'show user documents'


@app.route("/user/templates/")
def user_templates():
    return 'users templates'
