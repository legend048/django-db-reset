# first do "python manage.py flush"

# for reseting the migrations
# do "python manage.py shell"
# and run this in cli

# for PostgreSQL and many others
from django.db import connection

with connection.cursor() as cursor:
    # Fetch all tables
    cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
    tables = cursor.fetchall()
    # Drop all tables
    for table_name in tables:
        print(f"Dropping table: {table_name[0]}")
        cursor.execute(f'DROP TABLE "{table_name[0]}" CASCADE;')

# for sqlite
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        print(f"Dropping table: {table_name[0]}")
        cursor.execute(f'DROP TABLE IF EXISTS "{table_name[0]}";')
