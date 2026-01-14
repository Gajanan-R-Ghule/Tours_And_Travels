# import os
# import csv
# from django.core.management.base import BaseCommand
# from django.conf import settings
# from ei.models import payment


# class Command(BaseCommand):
#     help = 'Import data from CSV file'
    
#     def handle(self, *args, **options):
#         csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'csv', 'payment.csv')
        
#         with open(csv_file_path, 'r', encoding='utf-8') as file:
#             csv_reader = csv.DictReader(file)
            
#             for row in csv_reader:
#                 payment.objects.create(
#                     From=row['From'],
#                     To=row['To'],
#                     By_Train=row['By Train'],
#                     By_Road=row['By Road'],
#                     By_Air=row['By Air'],
#                 )
#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))