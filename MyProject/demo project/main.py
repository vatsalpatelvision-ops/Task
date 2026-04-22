from models import User
from database import engine , SessionLocal , Base

Base.metadata.create_all(bind=engine)

def create_user():
    db = SessionLocal()
    try:
        new_user = User(name="honey" , email="honey@gmail.com")
        # new_user = User(name="vatsal" , email="vatsal@gmail.com")

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(f"User is created with {new_user.id}")

    except Exception as e:
    
        db.rollback()
    finally:
        db.close()


def get_users():
    db = SessionLocal()

    try:
        users = db.query(User).all()

        for user in users:
            print(user.id , user.name , user.email)

    except Exception as e:
        pass
    
    finally:
        db.close()

def get_user_by_id(id):
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.id == id).first()
        # users = db.query(User).filter(User.name == "Alice").all() --> to find all the name with Alice

        print(user.name , user.email)
    except Exception as e:
        print("Invalid ID")
    finally:
        db.close()

if __name__ == "__main__":
    # create_user()
    # get_users()
    get_user_by_id(2)