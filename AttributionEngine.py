# Current syntax: python AttributionEngine.py CV=<CV> out=<outfile.txt>
# Holdout cross-validation, 70-30 split: CV=holdout30
# The validation results will be saved in <outfile.txt>
# It expects files called SelectedFeatures.txt and SelectedUsers.txt giving the 
# features and usernames chosen in newline separated format to be in the 
# current directory.

import os
import sys
import codecs
import Post
import FeatureExtractors as FE
import Algorithms

crossvalidation = 'none'
outputfile = None

# Extract commandline arguments
for arg in sys.argv:
  components = arg.split('=')
  if components[0] == "CV":
    crossvalidation = components[1]
  if components[0] == "out":
    outputfile = components[1]

f = open("SelectedUsers.txt",'r')
users = f.read().split('\n')
f.close()
del users[len(users)-1]
print("Training on users:")
for user in users:
  print("  "+user)

# Set up cross-validation, if there is any
if crossvalidation == 'file':
  f = open("SelectedTestDocuments.txt",'r')
  testDocs = f.read().split('\n')
  f.close()
  if testDocs[len(testDocs)-1] == "": del testDocs[len(testDocs)-1]
  testUsers = [""]*len(testDocs)
  testFiles =[[]]*len(testUsers)
  i = 0
  for line in testDocs:
    divided = line.split(':')
    testUsers[i] = divided[0]
    testFiles[i] = divided[1].split(' ')
    i += 1
elif crossvalidation[0:7] == 'holdout':
  holdout_percentage = float(crossvalidation[7:])
  print("\nPerforming holdout cross-validation (percentage: "+str(holdout_percentage)+")")
  holdout_percentage *= 0.01
  import random
  testUsers = users
  testFiles  = [[] for _ in range(0,len(testUsers),1)]
  for user in testUsers:
    dir = "../Data/"+user
    postfiles = os.listdir(dir)
    n = len(postfiles)
    n = int(float(n)*holdout_percentage)
    print(user+" "+str(n))
    idx = testUsers.index(user)
    for i in range(0,n,1):
      postidx = random.randrange(0,len(postfiles),1)
      testFiles[idx].append(postfiles.pop(postidx))
      try:
        f = open(dir+"/"+testFiles[idx][len(testFiles[idx])-1])
        f.close()
      except:
        print("Failure! user: " + "  " + user + "  file: " + testFiles[idx][len(testFiles[idx])-1])

# Now I want to construct feature extraction objects
f = open("SelectedFeatures.txt",'r')
featureNames = f.read().split('\n')
f.close()
features = []
for fName in featureNames:
  if fName == "numberofwords":
    features.append(FE.NumberOfWords())
  if fName == "complexity":
    features.append(FE.Complexity())
  if fName == "letterfraction":
    features.append(FE.LetterFraction())
  if fName == "uppercasefraction":
    features.append(FE.UppercaseFraction())
  if fName == "timeofposting":
    features.append(FE.TimeOfPosting())
  if fName == "numberofcharacters":
    features.append(FE.NumberOfCharacters())
  if fName == "whitespacefraction":
    features.append(FE.WhitespaceFraction())
  if fName == "charactersperword":
    features.append(FE.CharactersPerWord())
  if fName == "apostrophesperword":
    features.append(FE.ApostrophesPerWord())

print("\nUsing features:")
for feature in features:
  print("  "+feature.nickname)

print("\nExtracting feature vectors...")
featureVectors = []
classAssignments = []
for user in users:
  classification = users.index(user)
  print(" Extracting "+user)
  dir = "../Data/"+user
  posts = os.listdir(dir)
  try:
    idx = testUsers.index(user)
    tested = 1
  except:
    tested = 0
  for postfile in posts:
    if tested == 1:
      try:
        testFiles[idx].index(postfile)
        #print("  Omitting "+user+" "+postfile)
      except:
        tested = tested
    vec = []
    f = codecs.open(dir+"/"+postfile,'r',"utf-8")
    posttext = f.read()
    f.close()
    post = Post.Post(posttext)
    if len(post.words) == 0:
      continue
    i = 0
    for feature in features:
      vec.append(feature.Extract(post))
    featureVectors.append(vec)
    classAssignments.append(classification)

# Now it's time to run an ML algorithm!!!
classes = [0]*len(users)
for i in range(0,len(users),1):
  classes[i] = i

alg = Algorithms.MultinomialNaiveBayes()
alg.Learn(features, featureVectors, classes, classAssignments)

# Now comes the testing phase!
totalTests = 0
totalCorrect = 0
userAccuracy = [0]*len(testUsers)
for user in testUsers:
  dir = "../Data/"+user
  idx = testUsers.index(user)
  nUserDocs = 0
  print("Validating: " + user)
  for i in range(0,len(testFiles[idx]),1):
    file = testFiles[idx][i]
    f = codecs.open(dir+"/"+file,'r',"utf-8")
    posttext = f.read()
    f.close()
    post = Post.Post(posttext)
    if len(post.words) == 0:
      continue

    vec = []
    for feature in features:
      vec.append(feature.Extract(post))
    probabilities = alg.Predict(vec)
  
    # Determine the maximum probability
    max = -1
    maxIdx = -1
    for i in range(0,len(probabilities),1):
      if probabilities[i] > max:
        max = probabilities[i]
        maxIdx = i
    nUserDocs += 1
    totalTests += 1
    userIdx = users.index(user)
    if maxIdx == classes[userIdx]:
      userAccuracy[idx] += 1
      totalCorrect += 1
  if nUserDocs > 0:
    userAccuracy[idx] /= nUserDocs

overallAccuracy = totalCorrect/totalTests
print("\nOverall Accuracy: " + str(overallAccuracy) + "\n")
if (outputfile != None):
  f = open(outputfile, 'w')
  f.write("Overall Accuracy : " + str(overallAccuracy) + "\n")
for user in testUsers:
  print("  Accuracy for " + user + "  :  " + str(userAccuracy[testUsers.index(user)]))
  if (outputfile != None):
    f.write("Accuracy for " + str(users.index(user)) + "  :  " + str(userAccuracy[testUsers.index(user)]) + "\n")
      
