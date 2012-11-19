# Use this file to generate the 'SelectedUsers.txt' file required by the 
# attribution engine.
# syntax: python PostersGreaterThanN.py <# of posts>
# It will output all posters with at least <# of posts> posts
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
