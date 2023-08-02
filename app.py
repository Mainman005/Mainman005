from flask import Flask

from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)



# we need to import route.py here as our app.py doesnt know about routes.py file.
from routes import *
# we cant write this import at the top as first the app object has to initialized for routes.py to work.



if __name__ == "__main__":
    app.run(debug=True)
    

