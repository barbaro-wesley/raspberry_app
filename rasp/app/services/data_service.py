from app.repositories.data_repository import DataRepository


class DataService:
    def __init__(self):
        self.repository = DataRepository()

    def get_all_entries(self):
        entries = self.repository.get_all()
        return [{"id": e.id, "data": e.value} for e in entries]

    def add_entry(self, value: str):
        if not value or not value.strip():
            raise ValueError("O campo 'data' não pode ser vazio.")

        if len(value) > 500:
            raise ValueError("O valor não pode ter mais de 500 caracteres.")

        entry = self.repository.create(value.strip())
        return {"id": entry.id, "data": entry.value}

    def delete_entry(self, data_id: int):
        deleted = self.repository.delete(data_id)
        if not deleted:
            raise LookupError(f"Registro com id={data_id} não encontrado.")