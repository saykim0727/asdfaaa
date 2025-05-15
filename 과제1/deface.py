import requests
import hashlib
import time
import os
from datetime import datetime

class Defact:

  def __init__(self):
    if not os.path.exists("logs"):
      os.mkdir("logs")

    self.url = input("[!] URL을 입력하세요: ")
    if not self.url.startswith("https"):
      self.url = "https://" + self.url

    init_data, self.init_data_md5hash = self.getData()
    with open("logs/init.data","w") as f:
      f.write(init_data)

    print("[-] 현재 상태를 기준으로 위변조를 확인합니다")
  
  def diffData(self):
    data, data_md5hash = self.getData()
    time = datetime.now().strftime("%m%d_%H%M%S")
    if data_md5hash == self.init_data_md5hash:
      print("[O] 웹 사이트의 변경된 부분이 존재하지 않습니다")
    else:
      print("[X] 웹 사이트의 변경된 부분이 존재합니다.")
      print(f"    logs/diff_{time}.txt를 참조하여 변경된 부분을 확인하세요.")
      with open(f"logs/data_{time}","w") as f:
        f.write(data)
      os.system(f"diff logs/init.data logs/data_{time} > logs/diff_{time}.txt")

  def getData(self):
    data = requests.get(self.url).text
    md5sum = hashlib.md5()
    md5sum.update(data.encode())
    data_md5hash = md5sum.hexdigest()
    return data, data_md5hash
    
  def run(self):
    while True:
      time.sleep(3600)
      self.diffData()

if __name__ == "__main__":
  defact = Defact()
  defact.run()


