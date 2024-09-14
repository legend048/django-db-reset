
# Django Database and Migrations Reset Guide

This guide provides step-by-step instructions for completely resetting the Django database and migrations. It covers both PostgreSQL (and other databases) and SQLite.

## Step 1: Flush the Database

First, clear all data from your database using Django's `flush` command:

```bash
python manage.py flush
```

This command will remove all data from the database and reset sequences but keep the database schema (tables) intact. Type `yes` when prompted to confirm.

## Step 2: Reset the Migrations

To reset the migration history and drop all tables, follow these steps based on your database type.

### For PostgreSQL (and Other Databases)

1. Open the Django shell:

    ```bash
    python manage.py shell
    ```

2. Run the following Python code in the shell to drop all tables:

    ```python
    from django.db import connection

    with connection.cursor() as cursor:
        # Fetch all tables
        cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
        tables = cursor.fetchall()
        
        # Drop all tables
        for table_name in tables:
            print(f"Dropping table: {table_name[0]}")
            cursor.execute(f'DROP TABLE "{table_name[0]}" CASCADE;')
    ```

3. Exit the Django shell by typing `exit()`.

### For SQLite

1. Open the Django shell:

    ```bash
    python manage.py shell
    ```

2. Run the following Python code in the shell to drop all tables:

    ```python
    from django.db import connection

    with connection.cursor() as cursor:
        # Fetch all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        # Drop all tables
        for table_name in tables:
            print(f"Dropping table: {table_name[0]}")
            cursor.execute(f'DROP TABLE IF EXISTS "{table_name[0]}";')
    ```

3. Exit the Django shell by typing `exit()`.

## Step 3: Remove Migration Files

After dropping all tables, remove all migration files in each app's `migrations` folder. Keep the `__init__.py` file but delete all other `.py` files:

```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```

## Step 4: Recreate Migrations and Apply Them

Now that the database is reset and the migration files are removed, create fresh migrations and migrate the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Conclusion

These steps will reset your Django database to a clean state, allowing you to start fresh with new migrations. Be cautious when performing these operations, especially in a production environment, as they will delete all data.

---

Feel free to customize this guide further to fit your specific project needs.
