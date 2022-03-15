import random
import string
from database import db_session
from models import UserData

def login(email, password):
    queried_user = UserData.query.filter_by(email=email).first()
    # Check if email belongs to a registered user
    if hasattr(queried_user, "email"):
        # Verify their password
        if password == queried_user.password:
            authToken = "authToken: " + "".join(random.choices(
                string.ascii_lowercase + string.digits, k=23))
            return authToken
        else: # Wrong password
            return "bad credentials"
    else: # User does NOT exist
        return "bad credentials"

def signup(email, password):
    # If email address is already in use
    if UserData.query.filter_by(email=email).first() is not None:
        return "email in use"
    else:
        # Save new user record in the DB
        db_session.add(UserData(email=email, password=password))
        db_session.commit()
        print('New user signup: %s '% email)
        authToken = "authToken: " + "".join(random.choices(
            string.ascii_lowercase + string.digits, k=23))
        return authToken