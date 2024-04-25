import psycopg2

# Path to your SQL file containing the INSERT statements
sql_file_path = '2023.sql'

# Database connection parameters
db_params = {
    'database': 'database',
    'user': 'username',
    'password': 'password',
    'host': 'localhost',
    'port': 5432  # Default PostgreSQL port
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Read the SQL file
with open(sql_file_path, 'r') as file:
    sql_script = file.read()

# Split the script into individual INSERT statements
sql_commands = sql_script.split(';')

# Execute each INSERT statement
for command in sql_commands:
    if command.strip():
        try:
            cursor.execute(command)
            print(f"Successfully executed: {command}")
        except psycopg2.DatabaseError as e:
            print(f"Error executing {command}: {str(e)}")

# Commit changes and close the database connection
conn.commit()
conn.close()

print("All commands executed and committed successfully.")
