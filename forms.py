from flask_wtf import FlaskForm
# importing FlaskForm class from flask_wtf forms
from wtforms import StringField, SubmitField
# this are also classes in flask_wtf form for making text input and submit input type that we have seen in HTML.
from wtforms.validators import DataRequired
# importing datarequired class from wtfforms.validators

# for using wt_forms we need to define class for each forms and each class is class extened from flask form class.
class AddTaskForm(FlaskForm):
    # it will be having a title and a submit button. for that we will be creating instance of stringfield and submit field.
    
    # we will pass the label for the string field object as well as set the validator arguement , which is optional . so that no one cant post black fields. and to add that we need to import validators from wtf_forms. this keyword argument takes a list.
    title = StringField('Title', validators=[DataRequired()])
    # creating submit obejct with a label as argument
    submit = SubmitField('Submit')
    

class DeleteTaskForm(FlaskForm):
    submit = SubmitField("Delete")