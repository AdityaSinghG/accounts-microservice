"""
Account Model
"""

from service import db


class Account(db.Model):
    """
    Represents an Account
    """

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    disabled = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return f"<Account {self.name}>"

    def create(self):
        """
        Creates an Account
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        Updates an Account
        """
        db.session.commit()

    def delete(self):
        """
        Deletes an Account
        """
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """
        Converts Account to dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "disabled": self.disabled,
        }

    def deserialize(self, data):
        """
        Loads dictionary into Account
        """
        self.name = data.get("name")
        self.email = data.get("email")
        self.address = data.get("address")
        self.phone = data.get("phone")
        self.disabled = data.get("disabled", False)
        return self

    @classmethod
    def all(cls):
        """
        Returns all accounts
        """
        return cls.query.all()

    @classmethod
    def find(cls, account_id):
        """
        Finds account by id
        """
        return cls.query.get(account_id)
