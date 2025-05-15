import paramiko
import os
import time

name = "daangntestid"
pw = "daangnpwd123!"
script = "Daangn.sh"

def getServer():
  servers = []
  with open("host.txt","r") as f:
    while True:
      host = f.readline().strip()
      print(host)
      if not host: break
      servers.append(host)

  return servers

def scanServer(server):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh.connect(server, username=name, password=pw, timeout=10)
  except:
    print(f"[!] Can not connect to the {server}")
    ssh.close()
    return
  sess = paramiko.Transport((server, 22))
  sess.connect(username=name, password=pw)
  sftp = paramiko.SFTPClient.from_transport(sess)
  sftp.put("Daangn.sh", "/tmp/Daangn.sh")
  sftp.close()
  sess.close()

  ssh.exec_command("chmod 777 /tmp/Daangn.sh")
  stdin, stdout, _ = ssh.exec_command("/tmp/Daangn.sh")

  result = stdout.read().decode('utf-8')
  fname = f"report/{server}_report"
  f = open(fname, "w")
  f.write(result)
  f.close()
  ssh.close()

if __name__ == "__main__":
  if not os.path.exists("report"):
    os.mkdir("report")

  servers = getServer()

  for server in servers:
    scanServer(server)
