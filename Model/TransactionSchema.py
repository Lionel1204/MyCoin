from marshmallow import Schema, fields, post_load
from Transaction import Transaction
class TransactionSchema(Schema):
  fromMiner = fields.Str()
  toMiner = fields.Str()
  amount = fields.Integer()

  @post_load
  def make_transaction(self, data):
    return Transaction(**data)