from marshmallow import Schema, fields, validate


class DataInputSchema(Schema):
    data = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=500, error="O valor deve ter entre 1 e 500 caracteres.")
    )
