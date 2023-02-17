from flask import Flask, request, render_template
import db_processing

app = Flask(__name__)

events_data = {

}


@app.route("/vacancy/", methods=['GET', 'POST'])
def vacancy():
    if request.method == "POST":
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')
        table_data = {
            "vacancy_id": 1,
            "creation_date": "01-01-2022",
            "position_name": position_name,
            "company": company,
            "description": description,
            "contacts_id": contacts_id,
            "comment": comment,
            "user_id": 1
        }
        column = ", ".join(table_data.keys())
        placeholder = ':' + ', :'.join(table_data.keys())
        query = 'INSERT INTO vacancy (%s) VALUES (%s)' % (column, placeholder)
        db_processing.insert_info(query, table_data)

    result = db_processing.select_info('Select * from vacancy')
    return render_template('add-vacancy.html', all_vacancies=result)


@app.route("/vacancy/<vacancy_id>/", methods=['GET', 'PUT'])
def vacancy_id(vacancy_id):
    if request.method == 'PUT':
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')
        table_data = {
            "vacancy_id": 1,
            "creation_date": "01-01-2022",
            "position_name": position_name,
            "company": company,
            "description": description,
            "contacts_id": contacts_id,
            "comment": comment,
            "user_id": 1
        }
        query = f'UPDATE vacancy SET position_name = {position_name}, company = {company}, description = {description}, contacts_id={contacts_id}, comment = {comment}'
        db_processing.insert_info(query, table_data)
    result = db_processing.select_info('Select * from vacancy where vacancy_id = %s' % vacancy_id)
    return render_template('add-vacancy.html', all_vacancies=result)  # I think here should be different html template
    # for  put form. Please tell me if I'm wrong.


@app.route("/vacancy/<vacancy_id>/events/", methods=['GET', 'POST'])
def vacancy_events(vacancy_id):
    if request.method == "POST":
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        title = request.form.get('title')
        due_to_date = request.form.get('due_to_date')
        event_data = {
            'event_id': 1,
            'vacancy_id': 1,
            'description': description,
            'event_date': event_date,
            'title': title,
            'due_to_date': due_to_date,
            'status': 1
        }
        db_processing.insert_info('events', event_data)
    result = db_processing.select_info('Select * from events')
    return render_template('add_event.html', all_events=result)


@app.route("/vacancy/vacancy_id/events/event_id/", methods=['GET', 'PUT'])
def show_event_by_id(vacancy_id, event_id):
    # for event in events_data:
    # if event["vacancy_id"] == vacancy_id:
    #     list_of_events_for_vacancy.append(event)
    # for event_searcher in list_of_events_for_vacancy:
    #     if event_searcher["id"] == event_id:
    #         return list_of_events_for_vacancy.append(event_searcher)
    return


@app.route("/vacancy/vacancy_id/history/", methods=['GET'])
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


@app.route("/user/documents/", methods=['GET', 'POST', 'PUT'])
def user_documents():
    return 'show user documents'


@app.route("/user/templates/", methods=['GET', 'POST', 'PUT'])
def user_templates():
    return 'users templates'


if __name__ == "__main__":
    app.run()
