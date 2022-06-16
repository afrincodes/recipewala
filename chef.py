import mysql.connector
from flask import session, sessions

class chef_op:
    def connection(self):
        db=mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="recipewala")
        return db

    def chef_insert(self,name,email,mobile,password,city,state,photo):
        con=self.connection()
        sq="insert into chef_signup(name,email,mobile,password,city,state,photo) values(%s,%s,%s,%s,%s,%s,%s)"
        record = [name,email,mobile,password,city,state,photo]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return
    
    def chef_login_verify(self, email, password):
        con = self.connection()
        query = "select name,email from chef_signup where email=%s and password=%s"
        record = [email, password]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        rc = cursor.rowcount
        if rc == 0:
            return 0
        else:
            session['chef_email'] = email
            for r in row:
                session['name'] = r[0]
            return 1

    def chef_profile(self):
        con = self.connection()
        query = "select photo,name,email,mobile,city,state from chef_signup where email=%s"
        record = [session['chef_email']]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        return row


    def add_recipe(self,chef_email,name,ingredient,vntype,cuisine,description,photo):
        con=self.connection()
        sq="insert into add_recipe(chef_email,name,ingredient,vntype,cuisine,description,photo) values(%s,%s,%s,%s,%s,%s,%s)"
        record = [chef_email,name,ingredient,vntype,cuisine,description,photo]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return


    def chef_password_change(self,password):
        con=self.connection()
        sq="update chef_signup set password=%s where email=%s"
        record = [password,session['chef_email']]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return


    def chef_profile_delete(self):
        con=self.connection()
        sq="delete from chef_signup where email=%s"
        record = [session['chef_email']]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return

    def chef_dashboard(self):
        con = self.connection()
        query = "select recipe_id,name,vntype,cuisine,ingredient,description,photo,chef_email from add_recipe where chef_email=%s"
        record =[session['chef_email']]
        cursor = con.cursor()
        cursor.execute(query,record)
        row = cursor.fetchall()
        return row


    def recipe_delete(self,recipe_id):
        con = self.connection()
        query = "delete from add_recipe where recipe_id=%s"
        record = [recipe_id]
        mycursor=con.cursor()  
        mycursor.execute(query, record)
        con.commit()
        mycursor.close()
        con.close()
        return


    def chef_message(self):
        con = self.connection()
        query = "select message_id,name,user_email,message,reply from message m,user_signup u where m.user_email=u.email and chef_email=%s"
        record = [session['chef_email']]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        return row

    def chef_message_form(self,message_id):
        con = self.connection()
        query = "select message_id,message,reply from message where message_id=%s"
        record = [message_id]
        cursor = con.cursor()
        cursor.execute(query, record)
        row = cursor.fetchall()
        return row


    def chef_message_reply(self,message_id,reply):
        con=self.connection()
        sq="update message set reply=%s where message_id=%s"
        record = [reply,message_id]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return