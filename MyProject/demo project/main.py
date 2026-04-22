from models import User
from database import engine , SessionLocal , Base

Base.metadata.create_all(bind=engine)

def create_user():
    db = SessionLocal()
    try:
        new_user = User(name="harsh" , email="rajput@gmail.com")
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

def update_user_name(name , id):
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.id == id).first()

        user.name = name
        db.commit()
        db.refresh(user)
        print(f"user {id} updated with {user.name}")    
    except Exception as e:
        print("User not found")
    finally:
        db.close()


def delete_user_by_id(id):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == id).first()

        db.delete(user)
        db.commit()
        print("User Deleted")
    except Exception as e:
        print("User not found : ")
    finally:
        db.close()



if __name__ == "__main__":
    # create_user()
    # get_users()
    # get_user_by_id(2)
    # update_user_name("chintu",2)
    delete_user_by_id(3)
