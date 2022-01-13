from flask_login import UserMixin
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from . import db


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    first_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(1000))
    birthday = db.Column(DateTime(timezone=False), onupdate=func.now())
    created_at = db.Column(DateTime(timezone=False), onupdate=func.now())
    updated_at = db.Column(DateTime(timezone=False), onupdate=func.now())
    deleted_at = db.Column(DateTime(timezone=False), onupdate=func.now())
    avatar = db.Column(UUID(as_uuid=True))
    last_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    phone = db.Column(db.String(1000))
    title = db.Column(db.String(1000))
    address = db.Column(db.String(100))
    workplace_id = db.Column(db.String(1000))
    department = db.Column(db.String(1000))
    about = db.Column(db.String(100))
    full_name = db.Column(db.String(1000))


class Post_Assessment(UserMixin, db.Model):
    __table_args__ = {
        'schema': 'assessment'
    }
    __tablename__ = 'post_assessment'
    id = db.Column(UUID(as_uuid=True), primary_key=True)


class Accesor(UserMixin, db.Model):
    __table_args__ = {
        'schema': 'assessment'
    }
    __tablename__ = 'accesor'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    val = db.Column(db.Integer)
    role = db.Column(db.String(1000))


class Post(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    group_id = db.Column(UUID(as_uuid=True))
    user_id = db.Column(UUID(as_uuid=True))
    text = db.Column(db.String(1000))
    created_at = db.Column(DateTime(timezone=False), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=False), onupdate=func.now())
    deleted_at = db.Column(DateTime(timezone=False), onupdate=func.now())
    from_group = db.Column(db.Boolean)
    workplace_id = db.Column(db.String(1000))
    parent_id = db.Column(UUID(as_uuid=True))


class Post_Label(db.Model):
    __table_args__ = {
        'schema': 'assessment'
    }
    __tablename__ = 'post_label'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    id_post = db.Column(UUID(as_uuid=True))
    id_label = db.Column(UUID(as_uuid=True))
    elapsed_time = db.Column(DateTime(timezone=False))


class Accesor_Label(db.Model):
    __table_args__ = {
        'schema': 'assessment'
    }
    __tablename__ = 'accesor_label'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    id_accesor = db.Column(UUID(as_uuid=True))
    id_label = db.Column(UUID(as_uuid=True))
    create_time = db.Column(DateTime(timezone=False))


class Label(db.Model):
    __table_args__ = {
        'schema': 'assessment'
    }
    __tablename__ = 'labels'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    objectivity = db.Column(db.Integer)
    perspective = db.Column(db.Integer)
    doubts = db.Column(db.Integer)
    doubts_success = db.Column(db.Integer)
    meeting_needs = db.Column(db.Integer)
