import mysql.connector
from flask import session, sessions 

class user_op:
    def connection(self):
        db=mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="recipewala")
        return db

    def user_insert(self,name,email,mobile,password,city,state,photo):
        con=self.connection()
        sq="insert into user_signup(name,email,mobile,password,city,state,photo) values(%s,%s,%s,%s,%s,%s,%s)"
        record = [name,email,mobile,password,city,state,photo]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return


    def user_login_verify(self, email, password):
        con = self.connection()
        query = "select name,email from user_signup where email=%s and password=%s"
        record = [email, password]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        rc = cursor.rowcount
        if rc == 0:
            return 0
        else:
            session['user_email'] = email
            for r in row:
                session['name'] = r[0]
            return 1


    def user_profile(self):
        con = self.connection()
        query = "select photo,name,email,mobile,city,state from user_signup where email=%s"
        record = [session['user_email']]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        return row


    def user_password_change(self,password):
        con=self.connection()
        sq="update user_signup set password=%s where email=%s"
        record = [password,session['user_email']]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return

    def user_profile_delete(self):
        con=self.connection()
        sq="delete from user_signup where email=%s"
        record = [session['user_email']]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return

    

    def user_recipe(self):
        con = self.connection()
        query = "select c.photo,c.name,a.name,a.photo,a.vntype,a.cuisine,a.ingredient,recipe_id,chef_email from chef_signup c, add_recipe a  where c.email=a.chef_email"
        cursor = con.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row



    def user_recipe_details(self,recipe_id):
        con = self.connection()
        query = "select c.photo,c.name,a.name,a.photo,a.vntype,a.cuisine,a.ingredient,a.description from chef_signup c, add_recipe a  where c.email=a.chef_email and recipe_id=%s"
        record = [recipe_id]
        cursor = con.cursor()
        cursor.execute(query,record)
        row = cursor.fetchall()
        return row


    def user_message_insert(self,recipe_id,chef_email,message):
        con = self.connection()
        query = "insert into message(user_email,recipe_id,chef_email,message) values(%s,%s,%s,%s)"
        record = [session['user_email'],recipe_id,chef_email,message]
        cursor = con.cursor()
        cursor.execute(query,record)
        con.commit()
        cursor.close()
        con.close()
        return
    
    
    def user_message(self):
        con = self.connection()
        query = "select message_id,message,name,chef_email,reply from message m, chef_signup c where m.chef_email=c.email and user_email=%s"
        record = [session['user_email']]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        return row























    