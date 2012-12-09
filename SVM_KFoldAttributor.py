import sys
import numpy as np
import Helpers

from sklearn import svm

userFile = "SelectedUsers.txt"
featureFile = "SelectedFeatures.txt"
#discretFile = "Discretizations_2.pickle"

folds = 10

users = Helpers.LoadUsers(userFile)
n = len(users)

features = Helpers.LoadFeatures(featureFile, "")
print("\nUsing features:")
for feature in features:
  print("  "+feature.nickname)

classAssignments, featureVectors = Helpers.LoadData(users, features)
Helpers.ScaleData(featureVectors)

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

accuracies = np.array([0.]*folds)
#clf = svm.SVC(kernel='linear')
#clf = svm.SVC(kernel='rbf', gamma=0.04)
clf = svm.SVC(kernel='poly', degree=2, coef0=9., gamma=.5)

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
  #selFVs = np.array(selFVs)
  #testFVs = np.array(testFVs)

  # Do the learnin'
  selFVsT = np.transpose(selFVs);
  clf.fit(selFVs, selCA)

  # Now we validate
  print("Validating...")
  classifications = clf.predict(testFVs)
  for i in range(0,len(testCA),1):
    if classifications[i] == testCA[i]:
      accuracies[fold] += 1.

accuracies = accuracies/len(testCA)
print("Overall performance is: " + str(np.average(accuracies)))
