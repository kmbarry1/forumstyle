# arguments: <holdout %> <name of selected users file> <name of output file>
import os
import sys
import random

i = 0
fraction = 0.
users = []
output = None
for arg in sys.argv:
  if i == 1:
    fraction = float(arg)/100.
  if i == 2:
    f = open(arg, "r")
    users = f.read()
    f.close()
    users = users.split('\n')
    if users[len(users)-1] == "":
      del users[len(users)-1]
  if i == 3:
    output = arg
  i += 1

out = open(output, 'w')
for user in users:
  out.write(user+":")
  files = os.listdir("../Data/"+user)
  n = len(files)
  n = int(fraction * float(n))
  for i in range(0,n,1):
    postidx = random.randrange(0,len(files),1)
    out.write(files.pop(postidx)+" ") 
  out.write("\n")
out.close()
