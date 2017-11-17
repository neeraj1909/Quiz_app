import datetime
import json
import os

from django.contrib.auth.models import User

from Students.models import Question, Choice

HERE = os.path.dirname(__file__)


def import_questions_from_json():
    json_filepath = os.path.join(HERE, 'data/questions.json')
    with open(json_filepath, 'r') as f:
        questions_data = json.load(f)

    for question_data in questions_data:
        question = Question(
            question_text=question_data["question_text"],
            is_published=True,
            pub_date=datetime.datetime.utcnow())

        question.save()

        for choice_data in question_data['choices']:
            choice = Choice(
                question=question,
                choice_text=choice_data["choice_text"],
                is_correct=choice_data["is_correct"]
            )
            choice.save()


def main():
    questions_count = Question.objects.count()
    if questions_count > 0:
        print(f'{questions_count} Questions already exist in the database. Not importing form JSON.')
    else:
        import_questions_from_json()
        questions_count = Question.objects.count()
        print(f'Imported {questions_count} Questions form JSON.')

    # reset password for admin user
    admin_username = "admin"
    admin_password = "admin"
    try:
        admin_user = User.objects.get(username=admin_username)
    except User.DoesNotExist:
        admin_user = User(
            is_active=True,
            is_staff=True,
            is_superuser=True,
            username=admin_username,
            email='admin@playingwithcode.com',
        )

    admin_user.set_password(admin_password)
    admin_user.save()

    print(f'Admin username: {admin_username}')
    print(f'Admin password: {admin_password}')


if __name__ == "__main__":
    main()
