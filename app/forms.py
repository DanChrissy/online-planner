from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField, PasswordField,IntegerField, SelectMultipleField, DateField
from wtforms.validators import DataRequired, Email ,InputRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    name  = FileField('Meal Photo', validators = [FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])

class AccountForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    firstname = StringField('First Name', validators = [DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    dob = DateField('Date Of Birth',format = '%Y-%m-%d')

class ProfileFrom(FlaskForm):
    age = IntegerField('Age', validators=[Length(min = 2, max = 3)])
    allergies = StringField('Allergies', validators=[InputRequired()])
    illnesses = StringField('Illnesses', validators=[InputRequired()])
    foodPref = StringField('Food Prefernce', validators=[InputRequired()])
    caloriePref = StringField('Calorie Preference', validators=[InputRequired()])
    weightGoal = SelectField('Goal Objective',choices=[('20', '20'), ('40', '40'), ('60', '60'), ('80','80'),('100','100')])
    weightTime = SelectField('Time Objective',choices=[('2', '2'), ('4', '4'), ('12', '12'), ('24','24'),('52','52')])
    gender = SelectField(u'Gender', choices=[('Female', 'Female'), ('Male', 'Male')])
    weight = IntegerField('Weight', validators=[Length(min = 2, max = 6)])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()]) 

class MealForm(FlaskForm):
    mealName = StringField('Meal Name', validators = [InputRequired()])
    dateMeal = DateField('Meal Creation Date',format = '%Y-%m-%d')
    typeMeal = StringField('Meal Type', validators = [InputRequired()])
   
class RecipeForm(FlaskForm):
    recipeName = StringField('Recipe Name', validators = [InputRequired()])
    dateRecipe = DateField('Recipe Creation Date',format = '%Y-%m-%d')
    instructions = StringField('Instruction', validators = [InputRequired()])
    ingredients = SelectMultipleField(u'Ingredient Choices', choices = [('Vegan','Vegan'), ('Vegetarian','Vegetarian'),('Seafood','Seafood'),  ('Dairy-Free','Dairy-Free')])
