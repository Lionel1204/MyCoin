from Model.TransactionSchema import TransactionSchema
import json

def setTransaction(transaction):
  transListSchema = TransactionSchema(many=True)
  transSchema = TransactionSchema()
  newTrans = transSchema.load(transaction).data
  transactionList = getTransaction()
  transactionList.append(newTrans)

  json.dump(transListSchema.dump(transactionList).data, open('Transaction.json', 'w+'), encoding='utf-8')

def getTransaction():
  schema = TransactionSchema(many=True)
  with open('Transaction.json', 'r') as dataFile:
    data = dataFile.read()

  if len(data) < 1:
    return []

  content = schema.load(json.loads(data))
  return content.data