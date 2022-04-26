import sqlite3
from datetime import datetime

class Database:
    
    def __init__(self, db_name):
        with sqlite3.connect(db_name) as self.connect:      # make a connection
            self.cursor = self.connect.cursor()             # create a cursor

        self.create_table("""
        CREATE TABLE IF NOT EXISTS Posts (
            
            PostID                      integer     PRIMARY KEY     AUTOINCREMENT,
            Author                      text        NOT NULL        DEFAULT CURRENT_TIMESTAMP,
            QuestionTitle               text        NOT NULL,
            QuestionDescription         text        NOT NULL,
            DatePosted                  date        NOT NULL

        )""")
            
    def create_table(self, sql):
        """Creates a table using SQL passed into method

        Args:
            sql (str): SQL 
        """
        self.cursor.execute(sql)    #execute    = carry out
        self.connect.commit()       #commit     = save changes
        
    def query(self, sql, values):
        """Executes a query to the database
        
        Args:
            sql (str): SQL query to be executed
            values (tuple): Values to be used with the query
        """
        self.cursor.execute(sql, values) # say what to modify
        self.connect.commit()

    def get_post(self, post_id):
        sql = "SELECT * FROM Posts WHERE PostID=?"
        values = (post_id,)
        self.cursor.execute(sql, values)
        data = self.cursor.fetchone()
        return data

    def get_all_posts(self):
        sql = "SELECT * FROM Posts"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    def del_post(self, post_id):
        delete_sql = "DELETE FROM Posts WHERE PostID=?"
        self.query(delete_sql, (post_id,))
    
    def new_post(self, author, title, description):
        new_post_sql = """
        INSERT INTO Posts (Author, QuestionTitle, QuestionDescription, DatePosted) values (?,?,?,?)
        """
        
        # Get date for post
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")

        todays_date = f"{day}/{month}/{year}" # format string for DD/MM/YYYY
        
        values = (author, title, description, todays_date) #todays_date removed
        
        self.query(new_post_sql, values)


db = Database("forum_posts.db")