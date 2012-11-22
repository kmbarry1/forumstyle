allFeatures = ["numberofwords",
               "complexity",
               "letterfraction",
               "uppercasefraction",
               "timeofposting",
               "numberofcharacters",
               "whitespacefraction",
               "charactersperword",
               "apostrophesperword"]

import Post
import FeatureExtractors as FE
import codecs
import array
import os
import numpy as np

def ExtractFeature(feature):
  users = os.listdir("../Data/")
  vals = []
  limit = 50
  #deviations = np.array([0]*len(users))
  deviations = []
  j = 0
  for user in users:
    if j > limit: break
    files = os.listdir("../Data/"+user)
    if len(files) < 2:
      j += 1
      continue
    user_vals = []
#    print("user: " + user)
    i = 0
    for file in files:
      f = codecs.open("../Data/"+user+"/"+file, 'r', 'utf-8')
      posttext = f.read()
      f.close()
      post = Post.Post(posttext)
      if len(post.words) == 0: continue
      vvv = feature.Extract(post)
      vals.append(vvv)
      user_vals.append(vvv)
      i += 1
    deviations.append(np.std(np.array(user_vals)))
    print("mean for user " + user + " : " + str(np.average(np.array(user_vals))))
    j += 1
  vals = np.array(vals)
  deviations = np.array(deviations)
  return vals, deviations

def DetermineDiscretization(vals, deviations):
  vals = np.sort(vals)
  nExamples = len(vals)
  nUsers = len(deviations)
  avg_dev = np.average(deviations)
  # We need to split up the data in such a way that there is not a risk of 
  # overtraining (# discretiztaion bins < f*(# users) where f < 1) and we 
  # need to avoid low discrimination ability, which happens when there 
  # the discretization intervals are too wide. Additionally, these 
  # intervals should not be much smaller than the average variation in 
  # the quantity for a given user; otherwise we can't reliably classify that 
  # user.

  #nBins = nUsers/3

  max = np.max(vals)
  min = np.min(vals)
  #if ((max - min)/nBins < avg_dev):
  nBins = (max - min)/(avg_dev)
  # Now determine the bins
  n = 0
  bins = [0.]
  nPerBin = int(nExamples/nBins)

  # Some sensible limits on the bin occupancies and sizes.
  # The maximum width takes precedence over the minimum 
  # occupancy.
  min_occupancy = int(nPerBin)
  max_width = int(6) # in units of the average deviation, avg_dev

  idx = nPerBin
  epsilon = pow(10,-8) # potentially a bad idea, but should be fine for most features
  prev = 0.
  while idx < nExamples:
    next = vals[idx - 1] + epsilon
    if (abs(next - prev) > epsilon):
      if (next - prev < avg_dev):
        next = prev + avg_dev
        i = 1
        while Occupancy(vals, prev, next) < min_occupancy and i < max_width:
          next += avg_dev
          i += 1
        while idx < nExamples and vals[idx] <= next:
          idx += 1
      else:
        idx += nPerBin
      bins.append(next)
    else:
        idx += nPerBin
    prev = next
  return bins

def Occupancy(arr, min, max):
  # Determines the number of values v in sorted numpy array arr satisfying 
  # min <= v < max
  lower = np.searchsorted(arr, min, 'left')
  upper = np.searchsorted(arr, max, 'left')
  return upper - lower

# Now for the main script
features = []
for fName in allFeatures:
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

#discret_dict = {}
#i = 0
#for feature in features:
##  if i > 0: break
#  print("Doing feature " + feature.nickname)
#  v, dev = ExtractFeature(feature)
#  discret = DetermineDiscretization(v, dev)
#  discret_dict[feature.nickname] = discret
#  i += 1
#file = open("Discretizations.pickle",'wb')
#import pickle
#pickle.dump(discret_dict, file, pickle.DEFAULT_PROTOCOL)
#file.close()
