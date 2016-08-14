from app import db

from flask_sqlalchemy import abort

def add_to_db(obj):
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print  e
        raise Exception

    return True

