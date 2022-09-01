# pip install mysql
# pip install mysql.connector

from datetime import date
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="expense"    
)

cursor = con.cursor()

def registerUser(data):
    try:
        cursor.execute('INSERT INTO users (username, password, gender, name) VALUES (%s, %s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False
    
def login_page(data):
    print(data)
    try:
        cursor.execute('SELECT * FROM users WHERE username = %s and password = %s', data)
        return cursor.fetchone()
      
    except:
        return False
    
    
def addSources(data):
    print(data)
    
    try:
        cursor.execute('INSERT INTO incomesources (userId, source, income) VALUES (%s, %s, %s)', data)

        con.commit()
        return True
    except:
         return False
        
    
def allSources(id):
    try:
        cursor.execute('SELECT * FROM incomesources WHERE userId = %s', id)
        return cursor.fetchall()
    except:
        return False

def deleteSource(id):
    try:
        cursor.execute('DELETE FROM incomesources WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def singleSource(id):
    try:
        cursor.execute('SELECT source, income FROM incomesources WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False

def updateSource(data):
    try:
        cursor.execute('UPDATE incomesources SET source = %s, income = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False


def allExpCat(data):
    try:
        cursor.execute('SELECT * FROM expcat WHERE userId = %s', data)
        return cursor.fetchall()
    except:
        return False

def addExpCat(data):
    try:
        cursor.execute('INSERT INTO expcat (userId, name, type) VALUES (%s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False

def deleteExpCat(id):
    try:
        cursor.execute('DELETE FROM expcat WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False


def singleExpcat(id):
    try:
        cursor.execute('SELECT name, type FROM expcat WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False

def updateExpcat(data):
    try:
        cursor.execute('UPDATE expcat SET name = %s, type = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False


def getCat(data):
    try:
        cursor.execute('SELECT id, name, type FROM expcat WHERE userId = %s', data)
        return cursor.fetchall()
    except:
        return False


def addExpenses(data):
        print(data)
    
        try:
            cursor.execute('INSERT INTO expenses (userId, catId, amount, month) VALUES (%s, %s, %s, %s)', data)

            con.commit()
            return True
        except:
            return False


def allExpenses(data):
    try:
        cursor.execute('SELECT expenses.id, expcat.name, expenses.amount, expenses.month FROM expenses LEFT JOIN expcat ON expcat.id = catId WHERE expenses.userId = %s', data)
        return cursor.fetchall()
    except:
        return False

def deleteExpense(data):
    try:
        cursor.execute('DELETE FROM expenses WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def singleExpense(data):
    try:
        cursor.execute('SELECT expcat.id, expcat.name, expenses.amount, expenses.month FROM expenses LEFT JOIN expcat ON expcat.id = catId WHERE expenses.id = %s', data)
        return cursor.fetchone()
    except:
        return False

def updateExpenses(data):
    try:
        cursor.execute('UPDATE expenses SET catId = %s, amount = %s, month = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def getFilterExp(data):
    try:
        cursor.execute('SELECT expenses.id, expcat.name, expenses.amount, expenses.month FROM expenses LEFT JOIN expcat ON expcat.id = catId WHERE expenses.userId = %s and expenses.month = %s', data)
        return cursor.fetchall()
    except:
        return False
        
def addBudget(data):
    try:
        cursor.execute('INSERT INTO budget (userId, month, expAllowed) VALUES (%s, %s, %s)', data)

        con.commit()
        return True
    except:
         return False
        
def allBudget(data):
    try:
        cursor.execute('SELECT * FROM budget WHERE userId = %s', data)
        return cursor.fetchall()
    except:
        return False
    
def singleBudget(id):
    try:
        cursor.execute('SELECT * FROM budget WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False

def updateBudget(data):
    try:
        cursor.execute('UPDATE budget SET month = %s, expAllowed = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False    

def getBudget(data):
    try:
        cursor.execute('SELECT expAllowed FROM budget WHERE userId = %s and month = %s', data)
        return cursor.fetchone()
    except:
        return False