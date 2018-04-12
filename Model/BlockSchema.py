from Block import Block
from marshmallow import Schema, fields, post_load
from BlockDataSchema import BlockDataSchema
class BlockSchema(Schema):
  index = fields.Integer()
  timestamp = fields.DateTime()
  data = fields.Nested(BlockDataSchema)
  preHash = fields.Str()
  hash = fields.Str()

  @post_load
  def make_block(self, data):
    return Block(**data)