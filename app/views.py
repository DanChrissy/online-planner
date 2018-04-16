"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from forms import AccountForm,ProfileFrom,LoginForm, MealForm, RecipeForm, UploadForm
from models import UserAccount, UserProfile

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/addAcc', methods=['POST', 'GET'])
def addAcc():
    accForm = AccountForm()
    proForm = ProfileFrom()
    
    if request.method == 'POST' and accForm.validate_on_submit():
        user = accForm.username.data
        passW = accForm.password.data
        first = accForm.firstname.data
        last = accForm.lastname.data
        email = accForm.email.data
        date = accForm.dob.data
        
        userId = createId(first,user,passW)
        
        account = UserAccount(accountId = userId, username = user, password = passW, first_name = first, last_name = last, email = email, date_birth = date)
        db.session.add(account)
        db.session.commit()
    
       # acc = session.query(UserAccount).filter_by(username = user).first()
        #userAcc = UserAccount.query.filter_by(username = user).first()
        
        flash('Your account was saved successfully', 'success')
        return redirect(url_for('addProfile.html',form = proForm))
        
    flash_errors(accForm)
    return render_template('addAccount.html',form=accForm)

@app.route('/addProfile', methods = ['POST','GET'])
def addProfile():
    profileForm = ProfileFrom()
    
    if request.method == 'POST' and profileForm.validate_on_submit():
        
        user = profileForm.user.data
        gender = profileForm.user.data
        weight = profileForm.weight.data
        meals = request.form.getlist("meal_option")
        
        accountId = session.query(UserAccount).filter_by(username = user).first() 
        
        profile = UserProfile(accountId = accountId, gender = gender, weight = weight, meal = meals)
        db.session.add(profile)
        db.session.commit()
        
        flash('Your profile was saved successfully', 'success')
        return redirect(url_for('homepage'))
        
    flash_errors(profileForm)
    return render_template('addProfile.html',form=profileForm)


@app.route("/login", methods=["GET", "POST"])
def login():
    logForm = LoginForm()
    if request.method == "POST" and logForm.validate_on_submit():

        username = logForm.username.data
        password = logForm.password.data
            
        user = UserAccount.query.filter_by(username=username).first()
        pword = UserAccount.query.filter_by(password = password).first()
            
        login_user(user)

        # remember to flash a message to the user
        flash('Log in successful.', 'success')
        return redirect(url_for("homepage"))  # they should be redirected to a secure-page route instead
    return render_template("login.html", form=logForm)

@app.route('/homepage')
#@login_required
def homepage():
    return render_template('homepage.html')
    
@app.route('/addMeal', methods=["GET", "POST"])
@login_required
def addMeal():
    mealForm = MealForm()
    return render_template('addMeal.html', form = mealForm)

@app.route('/addRecipe')
@login_required
def addRecipe():
    recipeForm = RecipeForm()
    return render_template('addRecipe.html',form = recipeForm)
    
@app.route('/uploads')
#@login_required
def uploads():
    return render_template('uploads.html')

@app.route('/viewMeals')
def viewMeals():
    return render_template('viewMeals.html')
    
@app.route('/mealRecipe')
def mealRecipe():
    return render_template('mealRecipe.html')
    
@app.route('/supermarket')
def supermarket():
    return render_template('supermarket.html')

@app.route('/ingredients')
def ingredients():
    
    return render_template('ingredients.html')

@app.route('/changeIng')
def changeIng():
    return render_template('changeIng.html')
    
@app.route('/individualMeal')
def individualMeals():
    return render_template('individualMeals.html')

@app.route('/individualRecipe')
def individualRecipes():
    return render_template('individualRecipes.html')

@app.route('/searchRecipes')
def searchRecipes():
    return render_template('searchRecipes.html')
    
@app.route('/mealImage')
def mealImage():
    uploadForm = UploadForm()
    return render_template('mealImage.html',form = uploadForm)
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are now logged out","danger")
    """Render the website's about page."""
    return redirect(url_for("home"))

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserAccount.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

def createId(firstname,username,password):
    fname = firstname[:4]
    user = username[:4]
    Pass = password[:4]
    id = fname+user.upper()+Pass
    return id

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
