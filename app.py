from flask import Flask,render_template,request,redirect,url_for,session,flash
from chef import chef_op
from user import user_op
from captcha.image import ImageCaptcha
import random

app = Flask(__name__)          #object of class Flask
app.secret_key = "recipe wala"

@app.route('/')                 #redirect to the first page of app
def home():
    return render_template('index.html')          #this function will redirect to the html page




######################### CHEF SIGNUP_LOGIN_LOGOUT ############################

@app.route('/chef_signup')
def chef_signup():
    return render_template('chef_signup.html')



@app.route('/chef_signup_insert',methods=['POST','GET'])
def chef_signup_insert():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        mobile=request.form["mobile"]
        password=request.form["password"]
        city=request.form["city"]
        state=request.form["state"]
        photo=request.files["photo"]
        photo_name = photo.filename
        photo.save("static/chef/"  + photo_name)
        obj = chef_op()                             #chef module class object
        obj.chef_insert(name,email,mobile,password,city,state,photo_name)
        flash(" You were successfully registered!!")
        return render_template('chef_signup.html')


@app.route('/chef_login')
def chef_login():
    num=random.randrange(1000,9999)
    img = ImageCaptcha(width = 280, height = 90)    #create an image instance of the given size
    global captcha_text
    captcha_text = str(num)
    data = img.generate(captcha_text)
    img.write(captcha_text, 'static/images/CAPTCHA.png')        #write the image on the given file and save it
    return render_template('chef_login.html')


@app.route('/chef_login_verify',methods=['POST','GET'])
def chef_login_verify():
    if captcha_text!=request.form["captcha"]:
        ms="Invalid Captcha!!"
        return redirect(url_for('chef_login', msg=ms))
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        obj = chef_op()
        m=obj.chef_login_verify(email, password)
        if m == 0:
            ms="Invalid Email or Password"
            return render_template('chef_login.html',msg=ms)
        else:
            return redirect(url_for('chef_dashboard'))




@app.route('/chef_logout')
def chef_logout():
    session.clear()
    return redirect(url_for('chef_login'))



    


########################## USER SIGNUP_LOGIN_LOGOUT ###########################

@app.route('/user_signup')
def user_signup():
    return render_template('user_signup.html')


@app.route('/user_signup_insert',methods=['POST','GET'])
def user_signup_insert():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        mobile=request.form["mobile"]
        password=request.form["password"]
        city=request.form["city"]
        state=request.form["state"]
        photo=request.files["photo"]
        photo_name = photo.filename
        photo.save("static/user/"  + photo_name)
        obj = user_op()                             #chef module class object
        obj.user_insert(name,email,mobile,password,city,state,photo_name)
        flash(" You were successfully registered!!")
        return render_template('user_signup.html')


@app.route('/user_login')
def user_login():
    num=random.randrange(1000,9999)
    img = ImageCaptcha(width = 280, height = 90)
    global captcha_text
    captcha_text = str(num)
    data = img.generate(captcha_text)
    img.write(captcha_text, 'static/images/CAPTCHA.png')
    return render_template('user_login.html')


@app.route('/user_login_verify',methods=['POST','GET'])
def user_login_verify():
    if captcha_text!=request.form["captcha"]:
        ms="Invalid Captcha!!"
        return redirect(url_for('user_login', msg=ms))
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        obj = user_op()
        m=obj.user_login_verify(email, password)
        if m == 0:
            ms="Invalid Email or Password"
            return render_template('user_login.html',msg=ms)
        else:
            return redirect(url_for('user_dashboard'))


@app.route('/user_logout')
def user_logout():
    session.clear()
    return redirect(url_for('user_login'))



###################################################################



@app.route('/get_started')
def get_started():
    return render_template('get_started.html')


@app.route('/recipe')
def recipe():
    return render_template('recipe.html')


@app.route('/about')
def about():
    return render_template('about.html')

    
@app.route('/contact')
def contact():
    return render_template('contact.html')



####################### CHEF DASHBOARD & PROFILE, recipe_delete###################################

@app.route('/chef_dashboard')
def chef_dashboard():
    if 'chef_email' in session:
        obj=chef_op()
        record=obj.chef_dashboard()
        return render_template('chef_dashboard.html',rec=record)
    else:
        return redirect(url_for('chef_login'))


@app.route('/recipe_delete',methods=['POST','GET'])
def recipe_delete():
    if 'chef_email' in session:
        if request.method=='GET':  
            recipe_id=request.args.get("recipe_id")
            obj=chef_op() 
            obj.recipe_delete(recipe_id)
            flash("Recipe is succesfully deleted!!!")
            return redirect(url_for('chef_dashboard'))
    else:
        return redirect(url_for('chef_login'))


@app.route('/chef_profile')
def chef_profile():
    if 'chef_email' in session:
        obj=chef_op()
        record=obj.chef_profile()
        return render_template('chef_profile.html',chef_rec=record)
    else:
        return redirect(url_for('chef_login'))


################################### USER DASHBOARD & PROFILE, RECIPE, Message  ############################

@app.route('/user_dashboard')
def user_dashboard():
    if 'user_email' in session:
        return render_template('user_dashboard.html')
    else:
        return redirect(url_for('user_login'))

@app.route('/user_profile')
def user_profile():
    if 'user_email' in session:
        obj=user_op()
        record=obj.user_profile()
        return render_template('user_profile.html',user_rec=record)
    else:
        return redirect(url_for('user_login'))


@app.route('/user_recipe')
def user_recipe():
    if 'user_email' in session:
        obj=user_op()
        record=obj.user_recipe()
        return render_template('user_recipe.html', user_rec=record)
    else:
        return redirect(url_for('user_login'))


@app.route('/user_recipe_details',methods=['POST','GET'])
def user_recipe_details():
    if 'user_email' in session:
        if request.method=='GET':
            recipe_id=request.args.get('recipe_id')
            obj=user_op()
            record=obj.user_recipe_details(recipe_id)
            return render_template('user_recipe_details.html', user_rec=record)
    else:
        return redirect(url_for('user_login'))

@app.route('/user_recipe_search')
def user_recipe_search():
        if 'user_email' in session:
                return render_template('user_recipe_search.html')
        else:
                return redirect(url_for('user_login'))


@app.route('/user_message_form')
def user_message_form():
    if 'user_email' in session:
        obj=user_op()
        return render_template('user_message_form.html')
    else:
        return redirect(url_for('user_login'))

@app.route('/user_message_insert',methods=['POST','GET'])
def user_message_insert():
    if 'user_email' in session:
        if request.method=='GET' or  request.method=='POST':
            recipe_id=request.args.get('recipe_id')
            chef_email=request.args.get('chef_email')
            message = request.form['message']
            obj=user_op()
            obj.user_message_insert(recipe_id,chef_email,message)
            flash("Message submitted successfully!!!")
            return redirect(url_for('user_message_form'))
    else:
        return redirect(url_for('user_login'))


@app.route('/user_message')
def user_message():
    if 'user_email' in session:
        obj=user_op()
        record=obj.user_message()
        return render_template('user_message.html', user_rec=record)
    else:
        return redirect(url_for('user_login'))



######################################## Chef add_recipe ##########################

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')
    


@app.route('/add_recipe_insert',methods=['POST','GET'])
def add_recipe_insert():
    if request.method=='POST':
        chef_email=session["chef_email"]
        name=request.form["name"]
        ingredient=request.form["ingredient"]
        vntype=request.form["vntype"]
        cuisine=request.form["cuisine"]
        description=request.form["description"]
        photo=request.files["photo"]
        photo_name = photo.filename
        photo.save("static/chef/"  + photo_name)
        obj = chef_op()                             #chef module class object
        obj.add_recipe(chef_email,name,ingredient,vntype,cuisine,description,photo_name)
        flash("Recipe Added Successfully!!")
        return render_template('add_recipe.html')

@app.route('/chef_message')
def chef_message():
    if 'chef_email' in session:
        obj=chef_op()
        record=obj.chef_message()
        return render_template('chef_message.html',rec=record)
    else:
        return redirect(url_for('chef_login'))

@app.route('/chef_message_form',methods=['POST','GET'])
def chef_message_form():
    if 'chef_email' in session:
        if request.method=='GET':
            message_id=request.args.get('message_id')
            obj=chef_op()
            record=obj.chef_message_form(message_id)
            return render_template('chef_message_form.html',rec=record)
    else:
        return redirect(url_for('chef_login'))

@app.route('/chef_message_reply',methods=['POST','GET'])
def chef_message_reply():
    if 'chef_email' in session:
        if request.method=='GET' or  request.method=='POST':
            message_id=request.args.get('message_id')
            reply=request.form['reply']
            obj=chef_op()
            obj.chef_message_reply(message_id,reply)
            flash("Reply submitted successfully!!!")
            return redirect(url_for('chef_message'))
    else:
        return redirect(url_for('chef_login'))

#################################chef & user password change###############################################


@app.route('/chef_password')
def chef_password():
    if 'chef_email' in session:
        return render_template('chef_password.html')
    else:
        return redirect(url_for('chef_login'))

@app.route('/chef_password_change',methods=['POST','GET'])
def chef_password_change():
    if request.method=='POST':
        password=request.form["password"]
        obj = chef_op()                             #chef module class object
        obj.chef_password_change(password)
        session.clear()
        flash("You were successfully changed password!!")
        return redirect(url_for('chef_login'))
    


@app.route('/user_password')
def user_password():
    if 'user_email' in session:
        return render_template('user_password.html')
    else:
        return redirect(url_for('user_login'))

@app.route('/user_password_change',methods=['POST','GET'])
def user_password_change():
    if request.method=='POST':
        password=request.form["password"]
        obj = user_op()                             #chef module class object
        obj.user_password_change(password)
        session.clear()
        flash("You were successfully changed password!!")
        return redirect(url_for('user_login'))



#################################chef & user profile delete###############################################


@app.route('/chef_profile_delete')
def chef_profile_delete():
    if 'chef_email' in session:
        obj=chef_op()
        obj.chef_profile_delete()
        session.clear()
        flash("You were successfully deleted account!!")
        return redirect(url_for('home'))
    else:
        return redirect(url_for('chef_login'))


@app.route('/user_profile_delete')
def user_profile_delete():
    if 'user_email' in session:
        obj=user_op()
        obj.user_profile_delete()
        session.clear()
        flash("You were successfully deleted account!!")
        return redirect(url_for('home'))
    else:
        return redirect(url_for('user_login'))








if __name__=="__main__":
    app.run(debug=True)               #to activate app server