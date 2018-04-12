from marshmallow import Schema, fields, post_load
from TransactionSchema import TransactionSchema
from BlockData import BlockData
class BlockDataSchema(Schema):
  proofOfWork = fields.Integer()
  transactions = fields.List(fields.Nested(TransactionSchema))

  @post_load
  def make_blockdata(self, data):
    return BlockData(**data)