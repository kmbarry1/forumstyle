import Post
import FeatureExtractors as FE
import os
import string
import math
import codecs

setOfUsers = os.listdir("../Data")
count = 1
for user in setOfUsers:
   #user = os.listdir("../Data")[userNum]
   filesOfUser = os.listdir("../Data/"+user)
   numFilesOfUser = len(os.listdir("../Data/"+user))
   AllBigraphs = [[0 for col in range(26)] for row in range(26)]

   for fileToOpen in filesOfUser:
       f = codecs.open("../Data/"+user+"/"+fileToOpen,'r','utf-8')
       posttext = f.read()
       f.close

       post = Post.Post(posttext)

       nBigraph = FE.Bigraph()
       CurrentBigraph = nBigraph.Extract(post)
       for i in range(0,26):
          for j in range(0,26):
             AllBigraphs[i][j] = AllBigraphs[i][j]+CurrentBigraph[i][j]

   for i in range(0,26):
      for j in range(0,26):
         AllBigraphs[i][j] = float(AllBigraphs[i][j]) / float(numFilesOfUser)

   file = open("./StdDevFiles/name"+str(count)+".txt", "w")
   i = 0
   for arr in AllBigraphs:
      firstletter = string.ascii_lowercase[i]
      j = 0
      for val in arr:
         secondletter = string.ascii_lowercase[j]
         j += 1
         file.write(str(val) + "\n")          
      #file.write(firstletter + secondletter + " " + str(val) + "\n")
      i += 1
   file.close()
   count+=1
