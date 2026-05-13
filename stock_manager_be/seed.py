import sys
sys.path.insert(0, '.')

from database import SessionLocal, engine, Base
from passlib.context import CryptContext

# Initialize password context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    return pwd_context.hash(password)

# Import models after database setup
from models import User

# Create tables
Base.metadata.create_all(bind=engine)

# Get database session
db = SessionLocal()

try:
    # Check if users already exist
    admin_exists = db.query(User).filter(
        User.username == "admin"
    ).first()
    
    user_exists = db.query(User).filter(
        User.username == "user"
    ).first()
    
    # Add admin user if it doesn't exist
    if not admin_exists:
        admin_user = User(
            username="admin",
            email="admin@example.com",
            password=hash_password("admin")
        )
        db.add(admin_user)
        print("✓ Added admin user")
    else:
        print("✓ admin user already exists")
    
    # Add regular user if it doesn't exist
    if not user_exists:
        regular_user = User(
            username="user",
            email="user@example.com",
            password=hash_password("user")
        )
        db.add(regular_user)
        print("✓ Added user user")
    else:
        print("✓ user user already exists")
    
    db.commit()
    print("\n✓ Users seeded successfully!")
    
except Exception as e:
    print(f"✗ Error seeding users: {e}")
    db.rollback()

finally:
    db.close()
