from database import engine, Base, SessionLocal
from models import User

# Create tables
Base.metadata.create_all(bind=engine)


def create_user():
    db = SessionLocal()

    new_user = User(name="John", email="john@example.com")

    db.add(new_user)
    db.commit()
    db.close()


if __name__ == "__main__":
    create_user()
    print("User created!")