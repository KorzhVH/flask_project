from flask import Flask

app = Flask(__name__)

vacancy_data = [
    {"id": 1,
     "creation_date": "01.01.2023",
     "status": 1,
     "company": "some company",
     "contacts_id": [1, 2],
     "description": "It's something",
     "position_name": "Python Developer",
     "comment": "some comment",
     "user_id": 101
     },
    {"id": 2,
     "creation_date": "15.01.2023",
     "status": 1,
     "company": "some company",
     "contacts_id": [3, 4],
     "description": "It's something",
     "position_name": "Python Developer",
     "comment": "some comment",
     "user_id": 102
     },
    {"id": 3,
     "creation_date": "01.02.2023",
     "status": 1,
     "company": "some company",
     "contacts_id": [5, 6],
     "description": "It's something",
     "position_name": "Python Developer",
     "comment": "some comment",
     "user_id": 103
     }
]
events_data = [
    {"id": 1,
     "vacancy_id": 1,
     "description": "It's something",
     "event_date": "01.01.2024",
     "title": "Test Title",
     "due_to_date": "01.01.2030",
     "status": 1
     },
    {"id": 2,
     "vacancy_id": 2,
     "description": "It's something",
     "event_date": "15.01.2024",
     "title": "Test Title",
     "due_to_date": "01.01.2030",
     "status": 1
     },
    {"id": 3,
     "vacancy_id": 3,
     "description": "It's something",
     "event_date": "01.02.2025",
     "title": "Test Title",
     "due_to_date": "01.01.2030",
     "status": 1
     }
]


@app.route("/vacancy/", methods=['GET', 'POST'])
def vacancy():
    return vacancy_data


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
    for event_searcher in events_data:
        if event_searcher["vacancy_id"] == vacancy_id:
            list_of_events_for_vacancy.append(event_searcher)
    return list_of_events_for_vacancy[event_id]


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
