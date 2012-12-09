import sys
import numpy as np
import Algorithms
import Helpers

userFile = "SelectedUsers.txt"
featureFile = "SelectedFeatures.txt"
discretFile = "Discretizations.pickle"

folds = 10

users = Helpers.LoadUsers(userFile)
n = len(users)

features = Helpers.LoadFeatures(featureFile, discretFile)
print("\nUsing features:")
for feature in features:
  print("  "+feature.nickname)

classAssignments, featureVectors = Helpers.LoadData(users, features)

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

classes = [0]*n
for i in range(0,n,1):
  classes[i] = i

alg = Algorithms.MultinomialNaiveBayes()

accuracies = np.array([0.]*folds)

for fold in range(0,folds,1):
  print("Folding " + str(fold))
  selCA = []
  selFVs = np.array([])
  testCA = []
  testFVs = np.array([])
  for i in range(0,n,1):
    start = uniqueAuthorIndices[i]
    leaveout_beg = int(nDocsPerAuthor[i]/folds)*fold + start
    leaveout_end = leaveout_beg + int(nDocsPerAuthor[i]/folds)
    selCA.extend(classAssignments[start:leaveout_beg])
    selCA.extend(classAssignments[leaveout_end:uniqueAuthorIndices[i+1]])
    testCA.extend(classAssignments[leaveout_beg:leaveout_end])

    if i != 0:
      selFVs = np.append(selFVs, featureVectors[start:leaveout_beg], axis=0)
      testFVs = np.append(testFVs, featureVectors[leaveout_beg:leaveout_end], axis=0)
    else:
      selFVs = featureVectors[start:leaveout_beg]
      testFVs = featureVectors[leaveout_beg:leaveout_end]
    selFVs = np.append(selFVs, featureVectors[leaveout_end:uniqueAuthorIndices[i+1]], axis=0)
  selFVs = np.array(selFVs)
  testFVs = np.array(testFVs)

  # Do the learnin'
  alg.Learn(features, selFVs, classes, selCA)

  # Now we validate
  print("Validating...")
  for i in range(0,len(testCA),1):
    probabilities = alg.Predict(testFVs[i])
    pred = np.argmax(probabilities)
    if pred == testCA[i]:
      accuracies[fold] += 1.

accuracies = accuracies/len(testCA)
print("Overall performance is: " + str(np.average(accuracies)))
