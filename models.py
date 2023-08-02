from app import db
# this is the db instance that we have created on app.py file.

# we will be creating a class it will extend db.Model class.
class Task(db.Model):
    # defining column objects
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    # defining a special method in our class to represent each insrtance of our data model.
    def __repr__(self):
        return f"{self.title} created on {self.date}"

