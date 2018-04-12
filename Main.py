import requests
def main():
  u = requests.get("http://localhost:5000" + "/blocks").content
  print u

if __name__ == "__main__":
  main()