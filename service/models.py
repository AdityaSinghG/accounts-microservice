"""
Account Model
"""
from service import db


class Account(db.Model):
    """Account model for storing account data"""

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    date_joined = db.Column(db.Date(), nullable=False, default=db.func.current_date())

    def __repr__(self):
        return f"<Account {self.id} {self.name}>"

    def serialize(self):
        """Serialize account to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "date_joined": str(self.date_joined),
        }

    def deserialize(self, data):
        """Deserialize account from dictionary"""
        self.name = data["name"]
        self.email = data["email"]
        self.address = data["address"]
        self.phone = data["phone"]
        return self

    def create(self):
        """Create account in database"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update account in database"""
        db.session.commit()

    def delete(self):
        """Delete account from database"""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls):
        """Return all accounts"""
        return cls.query.all()

    @classmethod
    def find(cls, account_id):
        """Find account by id"""
        return cls.query.get(account_id)
