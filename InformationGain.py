import string
import copy
import numpy as np
import Helpers
import sys
import os
import AlgorithmsInfoGain

userFile = "SelectedUsers.txt"
featureFile = "SelectedFeatures.txt"
discretFile = "Discretizations.pickle"


# cutoff for 500 posts
os.system("python PostersGreaterThanN.py 500")
users = Helpers.LoadUsers(userFile)
n = len(users)

features = Helpers.LoadFeatures(featureFile,discretFile)

# classAssignments is the same as users
classAssignments, featureVectors = Helpers.LoadData(users, features)
print("# ass: " + str(len(classAssignments)))
print("# fv: " + str(len(featureVectors)))

uniqueAuthorIndices = [0]
ca = classAssignments[0]
for i in range(0,len(classAssignments),1):
  if ca != classAssignments[i]:
    ca = classAssignments[i]
    uniqueAuthorIndices.append(i)
uniqueAuthorIndices.append(len(featureVectors))
  
nDocsPerAuthor = [0]*n
for i in range(0,n,1):
  nDocsPerAuthor[i] = uniqueAuthorIndices[i+1] - uniqueAuthorIndices[i]
totalNumPosts = np.sum(nDocsPerAuthor)

# P(x = vf)
probOfRandomAuthor = nDocsPerAuthor / totalNumPosts
print('probOfRandomAuthor: ',probOfRandomAuthor)
# H(Y|x=vf)
alg = AlgorithmsInfoGain.MultinomialNaiveBayesInfoGain()
alg.LearnInfoGain(features,featureVectors,np.arange(n),classAssignments)
p_yub = alg.featureProbabilities # [j][l][b], j=features, l = classes (users), b = discritization


#H = -p*np.log2(p)
#test = np.isinf(H)
#H[test == 1] = 0


m = len(features)
k = [0]*m
for i in range(0,m,1):
  k[i] = len(features[i].discretization)

# Find H(Y)
# -----------------------------------------------
# sum probabilities over the users
p_yb = np.zeros((m,len(k)))
for y in range(0,m,1): # features
  for b in range(0,k[y]): # discretizations
    for u in range(0,n,1): # users
      p_yb[y][b] = p_yb[y][b] +  p_yub[y][u][b]*nDocsPerAuthor[u]
p_yb = p_yb/totalNumPosts

# sum over discretizations, b,  to get H(Y) = -sum(p_yb*log2(p_yb))
H_Y = np.zeros(m)
for y in range(0,m,1): # features
  for b in range(0,k[y]): # discretizations
    lp_yb = np.log2(p_yb[y][b])
    check = np.isinf(lp_yb)
    if(check == 1):
      lp_yb = 0
    H_Y[y] = H_Y[y] - p_yb[y][b]*lp_yb

# Find H(Y|X)
# --------------------------------------------
# Find H(Y|X=user) = -sum_bins -p_yub*log2(p_yub)

H_temp = np.zeros((m,n))
H_yx = np.zeros(m)
for y in range(0,m,1): # features
  for u in range(0,n,1): # users
    for b in range(0,k[y]): # discretizations
      lp_yub = np.log2(p_yub[y][u][b])
      check2 = np.isinf(lp_yub)
      if(check2 == 1):
        lp_yub = 0
      H_temp[y][u] = H_temp[y][u] - p_yub[y][u][b]*lp_yub
    H_yx[y] = H_yx[y] + probOfRandomAuthor[u]*H_temp[y][u]

IG = np.subtract(H_Y,H_yx)

f = open('topFeatures3','w')
NUM_MAX = 15
for i in range(0,NUM_MAX):
  ind = np.argmax(IG)
  print(features[ind].nickname,': ',IG[ind])
  value = (features[ind].nickname,': ',IG[ind])
  s = str(value)
  f.write(s)
  IG = np.delete(IG,ind)
  features = np.delete(features,ind)
