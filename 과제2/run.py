import paramiko

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
  sess = paramiko.Transport((server, 22))
  sess.connect(username=name, password=pw)
  sftp = paramiko.SFTPClient.from_transport(sess)
  sftp.put("Daangn.sh", "/tmp/Daangn.sh")
  sftp.close()
  t.close()
  sess.close()

  ssh.connect(server, username=name, password=pw)
  ssh.exec_command("chmod 777 /tmp/Daangn.sh")
  _, stdout, _ = ssh.exec_command("/tmp/Daangn.sh")
  
  result = stdout.read().decode('utf-8')
  print(result)

if __name__ == "__main__":
  servers = getServer()

  for server in servers:
    scanServer(server)
