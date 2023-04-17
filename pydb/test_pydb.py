from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.com import sessionmaker
import uuid

Base = declarative_base()


def generate_uuiud():
    return str(uuid.uuid4())

# Create a class inheriting from declarative_base we created earlier


class users(Base):
    # give the table a name
    __tablename__ = "users"
    # Create the userID column, make it primary, and generate a unique id
    userID = Column("userID", String, primary_key=True, default=generate_uuiud)

    # Create  the first name column and set the type to string
    # and create all the other columns
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    profileName = Column("profileName", String)
    email = Column("email", String)

    # Create the initializer for the class
    def __init__(self, firstName, lastName, profileName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.profileName = profileName
        self.email = email


class posts(Base):
    # Name the table "posts"
    __tablename__ = "posts"

    # Create the Primary Key Attribute which is the "postID" since every post
    # should have a unique ID
    postId = Column("postId", String, primary_key=True, default=generate_uuiud)

    # Create the "UserID" which is a Foreign key from "Users" Table
    userId = Column("userId", String, ForeignKey("users.UserID"))

    # Create the postContent attribute containing the Text the user posting
    postContent = Column("postContent", String)

    def __init__(self, userId, postContent):
        self.postContent = postContent
        self.userId = userId


# Give the database a Path and a Name to be created
db = "sqlite:///socialDB.db"
# Create SQLAlchemy engine which will connect to the db
engine = create_engine(db)
# Create the database along with the attributes
Base.metadata.create_all(bind=engine)

# Start a session to access the database
Session = sessionmaker(bind=engine)
session = Session()
