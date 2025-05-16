from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
class Follower (db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column (ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column (ForeignKey("user.id"))
    
    def serialize (self):
        return{
            "user_from_id": self.user_from_id.id,
            " user_to_id" : self.user_to_id.id

        }



class user(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firtsname: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post: Mapped[list["post"]] = relationship (back_populates = "user")
    comment: Mapped[list["comment"]] = relationship (back_populates ="user")



    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firsname": self.firsname,
            "lastname": self.lastname,
            "email": self.email
           
        }



class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[int] = mapped_column(String(120), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column (ForeignKey("post.id"))
    post: Mapped[list["post"]] = relationship(back_populates="Media")

    
   

    def serialize (self):
        return{
            "id": self.id,
            "type": self.type
        }



class post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["user"] = relationship (back_populates =("post"))
    comment: Mapped["comment"] = relationship (back_populates ="post")
    media: Mapped["Media"] = relationship (back_populates ="post")



    def serialize (self):
        return{
            "id": self.id,

        }

class comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(2000), unique=False, nullable=False)
    post_id: Mapped[int] = mapped_column (ForeignKey("post.id"))
    author_id: Mapped[int] = mapped_column (ForeignKey("user.id"))
    user: Mapped["user"] = relationship (back_populates ="comment")
    post: Mapped["post"] = relationship (back_populates = "comment")

    def serialize (self):
        return{
            "id": self.id,
            "comment_text": self.comment_text


        }




    




       

