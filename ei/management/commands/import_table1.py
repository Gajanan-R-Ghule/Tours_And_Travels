# import os
# import csv
# from django.core.management.base import BaseCommand
# from django.conf import settings
# from ei.models import Table1


# class Command(BaseCommand):
#     help = 'Import data from CSV file'
    
#     def handle(self, *args, **options):
#         csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'csv', 'table1.csv')
        
#         with open(csv_file_path, 'r', encoding='utf-8') as file:
#             csv_reader = csv.DictReader(file)
            
#             for row in csv_reader:
#                 Table1.objects.create(
#                     id=row['id'],
#                     state=row['State'],
#                     district=row['District'],
#                     name=row['Name'],
#                     category=row['Category'],
#                     image=row['Imgae'],
#                     desc=row['Description'],
#                     byair=row['ByAir'],
#                     bytrain=row['ByTrain'],
#                     byroad=row['ByRoad'],
#                 )
#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))