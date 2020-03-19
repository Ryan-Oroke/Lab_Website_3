import os
os.system("sudo /etc/init.d/postgresql start")
os.system("sudo -u postgres service postgresql start")
os.system("node server.js");