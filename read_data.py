import sqlite3

# 1. ភ្ជាប់ទៅកាន់ឯកសារមូលដ្ឋានទិន្នន័យ
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# 2. បញ្ជាឲ្យទាញយកទិន្នន័យទាំងអស់ពីតារាង 'users'
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

# 3. បង្ហាញលទ្ធផលនៅលើ terminal
print("ទិន្នន័យដែលមានក្នុង database.db:")
for user in all_users:
    print(user)