from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text

class User(Base):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    password = Column(String(64), nullable=False)
    age = Column(Integer)
    email = Column(String(50), unique=True)
    mobile = Column(String(11))
    isDelete = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.email}"