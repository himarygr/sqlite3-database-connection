import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('financial_data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for financial information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS financial_info (
        id INTEGER PRIMARY KEY,
        symbol TEXT,
        company_name TEXT,
        price REAL,
        market_cap REAL
    )
''')

# Insert sample data into the table
cursor.executemany('''
    INSERT INTO financial_info (symbol, company_name, price, market_cap)
    VALUES (?, ?, ?, ?)
''', [
    ('AAPL', 'Apple Inc.', 150.25, 2.5e12),
    ('GOOGL', 'Alphabet Inc.', 2750.60, 1.9e12),
    ('MSFT', 'Microsoft Corporation', 330.80, 2.8e12)
])

# Commit the changes and close the connection
conn.commit()
conn.close()

# Reconnect to the database
conn = sqlite3.connect('financial_data.db')
cursor = conn.cursor()

# Execute SQL queries to extract relevant financial information
cursor.execute('SELECT * FROM financial_info')
all_data = cursor.fetchall()

# Print the extracted data
print("All Financial Data:")
for row in all_data:
    print(row)

# Execute a more specific query
cursor.execute('SELECT company_name, price FROM financial_info WHERE price > 300')
filtered_data = cursor.fetchall()

# Print the filtered data
print("\nFiltered Financial Data (Price > 300):")
for row in filtered_data:
    print(row)

# Close the connection
conn.close()
