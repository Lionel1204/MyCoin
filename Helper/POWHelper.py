# If the block number is divided by 9, The coin is legal
def proofOfWork(lastProof):
  incrementor = lastProof + 1
  while not (incrementor % 9 == 0 and incrementor % lastProof == 0):
    incrementor += 1
  return incrementor