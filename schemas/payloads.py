from marshmallow import validate

from schemas import ma


class InputSchema(ma.Schema):
    """
    Input payload fields schema
    """
    subject = ma.Str(validate=validate.Length(min=1), required=True)
    sender_email = ma.Email(required=True)
    recipient_email = ma.Email(required=True)
    email_body = ma.Str(required=True, validate=validate.Length(min=2))
