# sDBlite

### A SQLite3 Wrapper

Welcome to the documentation for sDBlite, a lightweight Python wrapper for SQLite3 databases. This documentation will guide you through the features and usage of sDBlite, helping you leverage file-based SQL databases effortlessly.

## Introduction

Are you tired of dealing with the complexities of SQLite3 in your Python projects? Or are you simply looking for an easy way to implement a database system in your Python program? Look no further! sDBlite is here to simplify your database management tasks.

## Disclaimer: Test Purposes Only (Beta)

Before we begin, it's important to note that sDBlite is currently in the experimental phase. As a result, we do not recommend using it in large or sensitive projects. Please be aware that there is a risk of data loss when using this program.

## Installation

To start using sDBlite, follow these simple steps:

1. Download sDBlite from the repository [here](https://github.com/your-repository-link).

1. Extract the downloaded package to your desired location.

1. Import the `sDBlite` module in your Python program:

   ```python
   import sDBlite
   ```

## Getting Started

To get started with sDBlite, let's create a connection to a SQLite database file:

```python
# Connect to the database file
db = sDBlite.connect('path/to/your/database.db')
```

## Creating a Table

Next, let's create a table in the database. Define the table's columns and their corresponding data types using a dictionary:

```python
# Create a table named 'users'
columns = {
    'id': sDBlite.PrimaryKey,
    'first_name': str,
    'last_name': str,
    'age': int
}

# Create the table
users_table = db.table('users').create(columns)
```

## Inserting Data

Now, let's insert a row of data into the 'users' table:

```python
# Insert a row into the 'users' table
users_table.insert([1, 'John', 'Doe', 25])
```

## Retrieving Data

To retrieve data from the table, you can use the `select()` method:

```python
# Retrieve all rows from the 'users' table
rows = users_table.select()

# Print the retrieved data
for row in rows:
    print(row)
```

## Closing the Connection

Once you have finished working with the database, it's important to close the connection:

```python
# Close the database connection
db.close()
```

## Conclusion

sDBlite has not been officially released at this time. As a result, it is important to note that not all features of SQLite are currently wrapped within sDBlite. However, we are committed to continuous improvement and will be providing regular updates to enhance the program, incorporating new features and making it increasingly developer-friendly for your convenience.
