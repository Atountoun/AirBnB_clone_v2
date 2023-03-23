#!/usr/bin/python3
"""This module is used to set the database storage for the project
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """Object representation of the database storage."""

    __engine = None
    __session = None

    def __init__(self):
        """Storage initialisation method."""
        from models.base_model import Base

        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
                pool_pre_ping=True
                )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects depending of the class name `cls`
        if `cls`=None, all type of objects(User, State, City,Amenity,
        Place, Review
        """
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import Base

        classes = [City, State, Place, User, Review, Amenity]
        objects = {}
        if cls:
            classes = [cls]
        for class_name in classes:
            objs = self.__session.query(class_name).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database, create the current database
        session from the engine
        """
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )
        Session = scoped_session(session_factory)
        self.__session = Session()
