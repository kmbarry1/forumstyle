import os
import sys

users = os.listdir("./Data")

toplist = open("SelectedUsers.txt", 'w');
for user in users:
  n = len(os.listdir("../Data/"+user));
  if n >= int(sys.argv[1]):
    print(user+"  "+str(n))
    toplist.write(user+"\n")
toplist.close()