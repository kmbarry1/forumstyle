import pickle
import Discretizer

discret_dict = {}
i = 0
for feature in features:
#  if i > 0: break
  print("Doing feature " + feature.nickname)
  v, dev = ExtractFeature(feature)
  discret = DetermineDiscretization(v, dev)
  discret_dict[feature.nickname] = discret
  i += 1
file = open("Discretizations.pickle",'wb')
import pickle
pickle.dump(discret_dict, file, pickle.DEFAULT_PROTOCOL)
file.close()

