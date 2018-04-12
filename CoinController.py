from flask import Flask, request
from flask_marshmallow import Marshmallow

import BlockUtils
from Model.Transaction import Transaction
from Model.BlockData import BlockData
from Model.BlockSchema import BlockSchema
from Model.TransactionSchema import TransactionSchema

node = Flask(__name__)
ma = Marshmallow(node)

@node.route('/trans', methods=['POST'])
def createTrans():
  if request.method != 'POST':
    return ''

  BlockUtils.updateCoinTransaction(request.get_json())
  return 'Success to create a Transaction', 201


@node.route('/mine', methods=['GET'])
def mine():
  currentNodeTransactions = []
  blockChain = BlockUtils.getCurrentBlockChain()
  preBlock = blockChain[-1]
  preProof = preBlock.data.proofOfWork
  proof = BlockUtils.proofOfWork(preProof)

  newTrans = Transaction('network', BlockUtils.getMinerId(), 1)
  currentNodeTransactions.append(newTrans)

  newBlockData = BlockData(proof, list(currentNodeTransactions))

  newBlock = BlockUtils.createNextBlock(preBlock, newBlockData)

  blockChain.append(newBlock)
  BlockUtils.setLocalBlockChain(blockChain)
  return BlockSchema().dumps(newBlock).data

@node.route('/blocks', methods=['GET'])
def getBlockChain():
  blockChain = BlockUtils.getLocalBlockChain()
  return BlockSchema(many=True).dumps(blockChain).data

node.run()