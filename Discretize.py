import pickle
import Helpers
import Discretizer

features = Helpers.LoadFeatures("FeaturesToDiscretize.txt", "Discretizations.pickle")

discret_dict = {}
i = 0
for feature in features:
#  if i > 0: break
  print("Doing feature " + feature.nickname)
  v, dev = Discretizer.ExtractFeature(feature)
  discret = Discretizer.DetermineDiscretization(v, dev)
  discret_dict[feature.nickname] = discret
  i += 1

import pickle
try:
  file = open("Discretizations.pickle",'rb')
  official_discretizations = pickle.load(file)
  file.close()
except:
  official_discretizations = {}

for d in discret_dict:
  official_discretizations[d] = discret_dict[d]
file = open("Discretizations.pickle",'wb')
pickle.dump(official_discretizations, file, pickle.DEFAULT_PROTOCOL)
file.close()

