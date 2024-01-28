from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @staticmethod
    @validates('name')
    def validate_name(key, name):
        if not name:
            raise ValueError("Author must have a name.")
        return name

    @staticmethod
    @validates('phone_number')
    def validate_phone_number(key, phone_number):
        if phone_number and (len(phone_number) != 10 or not phone_number.isdigit()):
            raise ValueError("Author phone number must be exactly ten digits.")
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @staticmethod
    @validates('title')
    def validate_title(key, title):
        if not title:
            raise ValueError("Post must have a title.")
        return title

    @staticmethod
    @validates('content')
    def validate_content(key, content):
        if content and len(content) < 250:
            raise ValueError("Post content must be at least 250 characters long.")
        return content

    @staticmethod
    @validates('summary')
    def validate_summary(key, summary):
        if summary and len(summary) > 250:
            raise ValueError("Post summary must be a maximum of 250 characters.")
        return summary

    @staticmethod
    @validates('category')
    def validate_category(key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Post category must be either Fiction or Non-Fiction.")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'
