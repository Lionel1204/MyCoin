from datetime import datetime
from ConfigParser import ConfigParser
from Model.Block import Block
from Model.BlockSchema import BlockSchema
from Model.BlockData import BlockData
import Helper.BlockChainHelper as BCH
import Helper.TransactionHelper as TH
import Helper.NetHelper as NH
import Helper.POWHelper as POWH

#Need to manually construct the first block with this function
#Index=0, pre_hash=0
def createGenesisBlock():
  data = BlockData(1, [{'fromMiner':'', 'toMiner':'', 'amount':'0'}])
  return Block(0, datetime.now(), data, '0')

def createNextBlock(preBlock, data):
  return Block(preBlock.index + 1, datetime.now(), data, preBlock.hash)

# If the block number is divided by 9, The coin is legal
def proofOfWork(lastProof):
  return POWH.proofOfWork(lastProof)

def getLocalBlockChain():
  localChain = BCH.getLocalBlockChain()
  if len(localChain) == 0:
    BCH.setLocalBlockChain([createGenesisBlock()])
    localChain = BCH.getLocalBlockChain()
  return localChain

def setLocalBlockChain(chain):
  BCH.setLocalBlockChain(chain)

def getCurrentBlockChain():
  consensus()
  return getLocalBlockChain()

def updateCoinTransaction(transaction):
  TH.setTransaction(transaction)

def getMinerId():
  cp = ConfigParser()
  cp.read('config.ini')
  minerId = cp.get('base', 'miner.id')
  return minerId

def consensus():
  otherChains = getOtherChains()
  longestChain = BCH.getLocalBlockChain()

  if len(longestChain) == 0:
    longestChain = [createGenesisBlock()]

  for chain in otherChains:
    if len(longestChain) < len(chain):
      longestChain = chain

  BCH.setLocalBlockChain(longestChain)

def getOtherChains():
  cp = ConfigParser()
  cp.read('config.ini')
  urlStr = cp.get('servers', 'server.list')
  nodeUrls = urlStr.split(';')
  blockChains = []
  blockSchema = BlockSchema(many=True)
  for url in nodeUrls:
    blocks = NH.getBlocks(url)
    blockChains.append(blockSchema.loads(blocks).data)
  return blockChains
