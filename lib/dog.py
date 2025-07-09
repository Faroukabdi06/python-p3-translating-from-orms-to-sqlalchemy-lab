from models import Dog
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

def create_table(Base,engine):
    if __name__ == '__main__':
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)

def save(session,dog):
        # Session = sessionmaker(bind =engine)
        # session = Session()
        session.add(dog)
        session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name,breed=breed).first()

def update_breed(session, dog, breed):
    return session.query(Dog).update({
        Dog.breed:breed
    })