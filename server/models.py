from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError("Author must have a name")

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if phone_number and len(phone_number) == 10:
            return phone_number
        else:
            raise ValueError("The phone number must be exactly ten digits")

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name}, phone_number={self.phone_number})'
    
author = Author(name="agulu", phone_number='1324543331')

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('title')
    def validate_title(self, key, title):
        if title:
            return title
        else:
            raise ValueError("Post must have a title")

    @validates('content')
    def validate_content(self, key, content):
        if content and len(content) >= 250:
            return content
        else:
            raise ValueError("The post content must be at least 250 characters")

    @validates('summary')
    def validate_summary(self, key, summary):
        if summary and len(summary) <= 250:
            return summary
        else:
            raise ValueError("The post summary must be at most 250 characters")

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'

