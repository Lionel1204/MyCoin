import json
from Model.BlockSchema import BlockSchema

def setLocalBlockChain(chain):
  schema = BlockSchema(many=True)
  json.dump(schema.dump(chain).data, open('BlockChain.json', 'w+'), encoding='utf-8')

def getLocalBlockChain():
  schema = BlockSchema(many=True)
  with open('BlockChain.json', 'r') as dataFile:
    data = dataFile.read()

  if len(data) < 1:
    return []

  content = schema.load(json.loads(data))
  return content.data
