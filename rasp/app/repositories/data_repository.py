from app import db
from app.models.data import Data


class DataRepository:
    def get_all(self):
        return Data.query.all()

    def get_by_id(self, data_id):
        return db.session.get(Data, data_id)

    def create(self, value: str) -> Data:
        entry = Data(value=value)
        db.session.add(entry)
        db.session.commit()
        return entry

    def delete(self, data_id: int) -> bool:
        entry = self.get_by_id(data_id)
        if entry is None:
            return False
        db.session.delete(entry)
        db.session.commit()
        return True