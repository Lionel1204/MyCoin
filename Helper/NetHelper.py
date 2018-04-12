import requests

def getBlocks(url):
  resp = requests.get(url + "/blocks")
  if resp.status_code == requests.codes.ok:
    return resp.content
  else:
    return []

