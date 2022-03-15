from sqlalchemy import Integer,String,Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UserData(Base):
    """user account"""

    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String(255), unique=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return str(self.email)

