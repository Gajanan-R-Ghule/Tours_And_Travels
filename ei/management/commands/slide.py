# import os
# import csv
# from django.core.management.base import BaseCommand
# from django.conf import settings
# from ei.models import Slide


# class Command(BaseCommand):
#     help = 'Import data from CSV file'
    
#     def handle(self, *args, **options):
#         csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'csv', 'slide.csv')
        
#         with open(csv_file_path, 'r', encoding='utf-8') as file:
#             csv_reader = csv.DictReader(file)
            
#             for row in csv_reader:
#                 Slide.objects.create(
#                     # id=row['id'],
#                     name=row['name'],
#                     image=row['image'],
#                 )
#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))