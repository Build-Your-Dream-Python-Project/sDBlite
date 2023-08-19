# In this code, I'll show you
# How to:
# COnnect to a database(In this case file.txt)
# Create a table
# Insert Data into the table
# Fetch Data from It
# Drop(Delete/Remove) the table
# Commit the changes and Close the connection to the database

#
#
# Please ensure that you download and include "sdb.py" in your current Python code directory.
#
#

import sdb  # Import the sdb module

# Connect to the SQLite database file 'file.txt' with logging enabled
db_object = sdb.connect('file.txt', log=True)

# Define the columns for the 'users' table
columns = {
    'id': sdb.PrimaryKey,  # Primary key column for unique identification
    'firstname': str,  # Column for storing first names as strings
    'lastname': str,  # Column for storing last names as strings
    'age': int,  # Column for storing age as integers
}

# Create the 'users' table with the defined columns and logging enabled
tusers = db_object.table("users").create(columns, log=True)

# Insert a row of data [1, 'John', 'Doe', 25] into the 'users' table with logging enabled
tusers.insert([1, 'John', 'Doe', 25], log=True)

# Insert another row of data [2, 'Jane', 'Smith', 30] into the 'users' table with logging enabled
tusers.insert([2, 'Jane', 'Smith', 30], log=True)

# Retrieve all rows from the 'users' table
rows = tusers.select()

# Print each row of data retrieved from the 'users' table
for row in rows:
    print(row)

# Drop (delete) the 'users' table with logging enabled
tusers.drop(log=True)

# Close the connection to the database file with logging enabled
db_object.close(log=True)
