from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):
    username = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=80, error="O usuário deve ter entre 3 e 80 caracteres.")
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=6, error="A senha deve ter pelo menos 6 caracteres.")
    )


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
