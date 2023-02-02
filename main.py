from flask import Flask

app = Flask(__name__)


@app.route("/vacancy/", methods=['GET', 'POST'])
def vacancy():
    return 'any vacancy'


@app.route("/vacancy/id/", methods=['GET', 'DELETE'])
def vacancy_id():
    return 'vacancy by id'


@app.route("/vacancy/id/events/", methods=['GET', 'POST', 'DELETE'])
def vacancy_events():
    return 'show all events'


@app.route("/vacancy/id/events/event_id/", methods=['GET', 'PUT', 'DELETE'])
def show_event_by_id():
    return 'show event by id'


@app.route("/vacancy/id/history/", methods=['GET', 'DELETE'])
def vacancy_history():
    return 'any vacancy'


@app.route("/user/", methods=['GET'])
def get_user_main_page():
    return 'any vacancy'


@app.route("/user/calendar/", methods=['GET'])
def user_calendar():
    return 'show user calendar'


@app.route("/user/mail/", methods=['GET'])
def user_mail():
    return 'show users mail box '


@app.route("/user/settings/", methods=['GET', 'PUT'])
def user_settings():
    return 'any vacancy'


@app.route("/user/documents/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_documents():
    return 'show user documents'


@app.route("/user/templates/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_templates():
    return 'users templates'
