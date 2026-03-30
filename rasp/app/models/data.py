from app import db


class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Data {self.id}: {self.value}>"