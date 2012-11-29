import copy
import numpy as np

class LearningAlgorithm:
  def Learn(self, features, featureVectors, classes, assignments):
    print("Studying hard!")

  def Predict(self, featureVectors):
    print("You will die young.")

class MultinomialNaiveBayes(LearningAlgorithm):
  def Learn(self, features, featureVectors, classes, assignments):
    print("You're so naive.")

    self._features = copy.deepcopy(features)
    n = len(features)
    m = len(featureVectors)
    c = len(classes)
    k = [0]*n
    for i in range(0,n,1):
      k[i] = len(features[i].discretization)

    self.classProbabilities = [0]*c
    self.featureProbabilities = [[]]*n

    for i in range(0,n,1):
      self.featureProbabilities[i] = [[]]*c

    for i in range(0,n,1):
      for j in range(0,c,1):
        self.featureProbabilities[i][j] = [1]*k[i] # Initialize to 1 for Laplace smoothing

    for l in range(0,c,1):
       for i in range(0,m,1):
         if assignments[i] == classes[l]:
           self.classProbabilities[l] += 1
       self.classProbabilities[l] /= m

    numClassExamples = [0]*c
    for i in range(0,c,1):
      numClassExamples[i] = assignments.count(classes[i])

    for j in range(0,n,1):
      for b in range(0,k[j],1):
        for l in range(0,c,1):
          for i in range(0,m,1):
            if b < k[j] - 1:
              if (featureVectors[i][j] >= features[j].discretization[b] and featureVectors[i][j] < features[j].discretization[b+1] and assignments[i] == classes[l]):
                self.featureProbabilities[j][l][b] += 1
            else:
              if (featureVectors[i][j] >= features[j].discretization[b] and assignments[i] == classes[l]):
                self.featureProbabilities[j][l][b] += 1
          self.featureProbabilities[j][l][b] = self.featureProbabilities[j][l][b] / (numClassExamples[l] + k[j])

    print("All done!")

  def Predict(self, featureVector):
    n = len(self.featureProbabilities)
    c = len(self.classProbabilities)
    k = [0]*n
    for i in range(0,n,1):
      k[i] = len(self.featureProbabilities[i][0])

    predictedProbabilities = [1]*c

    for l in range(0,c,1):
      pOfy = self.classProbabilities[l]
      pOfxGiveny = 1
      pOfx = 0
      for ll in range(0,c,1):
        probProd = 1
        for j in range(0,n,1):
          value = -1
          for i in range(0,k[j],1):
            if i < k[j] - 1:
              if featureVector[j] >= self._features[j].discretization[i] and featureVector[j] < self._features[j].discretization[i+1]:
                value = i
            else:
              if featureVector[j] >= self._features[j].discretization[i]:
                value = i
          probProd *= self.featureProbabilities[j][ll][value]
        if l == ll: pOfxGiveny = probProd
        pOfx += self.classProbabilities[ll]*probProd
      predictedProbabilities[l] = pOfy*pOfxGiveny/pOfx

    return predictedProbabilities
