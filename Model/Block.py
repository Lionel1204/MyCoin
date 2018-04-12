import hashlib
'''
Block structure:
{
  'hash'
  'index'
  'data'
  'timestamp'
  'preHash'
}
'''

class Block():
  def __init__(self, index, timestamp, data, preHash, hash=None):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.preHash = preHash
    if hash is None:
      self.hash = self.genHash()
    else:
      self.hash = hash

  def genHash(self):
    sha = hashlib.sha256()
    sha.update(str(self.index)
             + str(self.timestamp)
             + str(self.data)
             + str(self.preHash))
    return sha.hexdigest()
