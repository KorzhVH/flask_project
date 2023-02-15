from flask import Flask, request, render_template
import db_processing
app = Flask(__name__)

vacancy_data = [
    {"id": "int",
     "creation_date": "text",
     "status": "int",
     "company": "text",
     "contacts_id": [],
     "description": "text",
     "position_name": "text",
     "comment": "text",
     "user_id": "int"
     },
]
events_data = [
    {"id": "int",
     "vacancy_id": "int",
     "description": "text",
     "event_date": "text",
     "title": "text",
     "due_to_date": "text",
     "status": "int"
     },
]


tables = {
    "vacancy_table": {
        "position_name": "",
        "company": "",
        "description": "",
        "contacts_id": "",
        "comment": "",
    }
}

@app.route("/vacancy/", methods=['get', 'post'])
def vacancy():
    if request.method =="post":
       position_name = request.form.get['position_name']
       company = request.form.get['company']
       description = request.form.get['description']
       contacts_id = request.form.get['contacts_id']
       comment = request.form.get['comment']


    return render_template('add-vacancy.html')


@app.route("/vacancy/vacancy_id/", methods=['GET', 'DELETE'])
def vacancy_id(vacancy_id):
    for vacancy_searcher in vacancy_data:
        if vacancy_searcher["vacancy_id"] == vacancy_id:
            return vacancy_searcher


@app.route("/vacancy/vacancy_id/events/", methods=['GET', 'POST', 'DELETE'])
def vacancy_events(vacancy_id):
    list_of_events_for_vacancy = []
    for event_searcher in events_data:
        if event_searcher["vacancy_id"] == vacancy_id:
            list_of_events_for_vacancy.append(event_searcher)
    return list_of_events_for_vacancy


@app.route("/vacancy/vacancy_id/events/event_id/", methods=['GET', 'PUT', 'DELETE'])
def show_event_by_id(vacancy_id, event_id):
    list_of_events_for_vacancy = []
    for event in events_data:
        if event["vacancy_id"] == vacancy_id:
            list_of_events_for_vacancy.append(event)
    for event_searcher in list_of_events_for_vacancy:
        if event_searcher["id"] == event_id:
            return list_of_events_for_vacancy.append(event_searcher)


@app.route("/vacancy/vacancy_id/history/", methods=['GET', 'DELETE'])
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


if __name__ == "__main__":
    app.run()
