import csv
from django.core.management.base import BaseCommand
from analytics.models import UserForm, Suggestions

class Command(BaseCommand):
    help = 'Export UserForm and Suggestions data to separate CSV files'

    def handle(self, *args, **options):
        user_form_file_path = 'user_form_data.csv'
        suggestions_file_path = 'suggestions_data.csv'
        
        # Get all UserForm instances
        user_forms = UserForm.objects.all()

        # Write UserForm data to CSV file
        with open(user_form_file_path, 'w', newline='') as csv_file:
            fieldnames_user_form = ['id', 'question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames_user_form)

            # Write header
            writer.writeheader()

            # Write data
            for user_form in user_forms:
                writer.writerow({
                    'id': user_form.id,
                    'question1': user_form.question1,
                    'answer1': user_form.answer1,
                    'question2': user_form.question2,
                    'answer2': user_form.answer2,
                    'question3': user_form.question3,
                    'answer3': user_form.answer3,
                    'question4': user_form.question4,
                    'answer4': user_form.answer4,
                })

        self.stdout.write(self.style.SUCCESS(f'UserForm data exported to {user_form_file_path}'))

        # Get and write Suggestions data to CSV file
        suggestions = Suggestions.get_all_firestore()

        with open(suggestions_file_path, 'w', newline='') as csv_file:
            fieldnames_suggestions = ['id', 'suggestion']

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames_suggestions)

            # Write header
            writer.writeheader()

            # Write data
            for suggestion in suggestions:
                writer.writerow({
                    'id': suggestion['id'],
                    'suggestion': suggestion['suggestion'],
                })

        self.stdout.write(self.style.SUCCESS(f'Suggestions data exported to {suggestions_file_path}'))
