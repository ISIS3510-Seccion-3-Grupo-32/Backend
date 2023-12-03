import csv
from django.core.management.base import BaseCommand
from analytics.models import UserForm

class Command(BaseCommand):
    help = 'Export UserForm data to a CSV file'

    def handle(self, *args, **options):
        file_path = 'user_form_data.csv'  # Change the file path as needed

        # Get all UserForm instances
        user_forms = UserForm.objects.all()

        # Write data to CSV file
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['id', 'question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

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

        self.stdout.write(self.style.SUCCESS(f'Data exported to {file_path}'))
