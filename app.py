from flask import Flask, request, render_template
import alch_db
from models import Vacancy, Events

app = Flask(__name__)

events_data = {

}


@app.route("/vacancy/", methods=['GET', 'POST'])
def vacancy():
    alch_db.init_db()
    if request.method == "POST":
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')
        current_vacancy = Vacancy(200, position_name, company, description, contacts_id, comment, 1)
        alch_db.db_session.add(current_vacancy)
        alch_db.db_session.commit()
        get_result = alch_db.db_session.query(Vacancy).all()
        return render_template('add-vacancy.html', all_vacancies=get_result)
    else:
        get_result = alch_db.db_session.query(Vacancy).all()
        return render_template('add-vacancy.html', all_vacancies=get_result)


@app.route("/vacancy/<vacancy_id>/", methods=['GET', 'POST'])
def vacancy_id(vacancy_id):
    alch_db.init_db()
    if request.method == 'POST':
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')
    else:
        get_result = alch_db.db_session.query(Vacancy).where(Vacancy.vacancy_id == vacancy_id).all()
        return render_template('add-vacancy.html', all_vacancies=get_result)


@app.route("/vacancy/<vacancy_id>/events/", methods=['GET', 'POST'])
def vacancy_events(vacancy_id):
    alch_db.init_db()
    if request.method == "POST":
        event_id = request.form.get('event_id')
        title = request.form.get('title')
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        due_to_date = request.form.get('due_to_date')
        curr_event = Events(event_id, vacancy_id, title, description, event_date, due_to_date, 100)
        alch_db.db_session.add(curr_event)
        alch_db.db_session.commit()
        get_result = alch_db.db_session.query(Vacancy).all()
        return render_template('add-vacancy.html', all_vacancies=get_result)
    else:
        get_result = alch_db.db_session.query(Events).all()
        return render_template('add_event.html', all_events=get_result)


@app.route("/vacancy/<vacancy_id>/events/<event_id>/", methods=['GET', 'POST'])
def show_event_by_id(vacancy_id, event_id):
    alch_db.init_db()
    if request.method == 'POST':
        pass
    else:
        get_result = alch_db.db_session.query(Events).where(Events.event_id == event_id, Events.vacancy_id == vacancy_id)
        return render_template('add_event.html', all_events=get_result)


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
