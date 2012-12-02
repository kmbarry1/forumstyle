import string
import copy
import numpy as np

class FeatureExtractor:
  def Extract(self, post):
    print("Needs to be overridden in derived class")

  nickname = "FE Base Class"

class NumberOfWords(FeatureExtractor):
  def Extract(self, post):
    return len(post.words)

  nickname = "numberofwords"
  discretization = [0, 3, 6, 10, 15, 30, 60, 120, 240, 500 ]

class Complexity(FeatureExtractor):
  # (# of unique words)/(# of words)
  def Extract(self, post):
    wordlist = copy.copy(post.words)
    numWords = len(wordlist)
    numUniqueWords = 0
    while len(wordlist) != 0:
      numUniqueWords += 1
      word = wordlist.pop(0);
      i = 0
      while i != len(wordlist):
        if (word == wordlist[i]):
          del wordlist[i]
          i -= 1
        i += 1
    return float(numUniqueWords)/float(numWords)

  nickname = "complexity"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFraction(FeatureExtractor):
  # Fraction of all characters that are letters
  def Extract(self, post):
    numCharacters = len(post.fulltext)
    numLetters = 0
    for c in post.fulltext:
      if string.ascii_letters.find(c) != -1:
        numLetters += 1
    if numCharacters > 0:
      return float(numLetters)/float(numCharacters)
    else:
      return 0

  nickname = "letterfraction"
  discretization = [ 0, 0.3, 0.6, 0.75, 0.8, 0.85, 0.9 ]

class UppercaseFraction(FeatureExtractor):
  # Count what fraction of all letters uppercase letters are
  def Extract(self, post):
    numCaps = 0
    numLetters = 0
    for c in post.fulltext:
      if string.ascii_letters.find(c) != -1:
        numLetters += 1
      if string.ascii_uppercase.find(c) != -1:
        numCaps += 1
    if numLetters > 0:
      return float(numCaps)/float(numLetters)
    else:
      return 0

  nickname = "uppercasefraction"
  discretization = [ 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.4, 0.7 ]

class TimeOfPosting(FeatureExtractor):
  def Extract(self, post):
    return float(post.time)

  nickname = "timeofposting"
  discretization = [ 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410 ]

class NumberOfCharacters(FeatureExtractor):
  def Extract(self, post):
    return float(len(post.fulltext))

  nickname = "numberofcharacters"
  discretization = [ 0, 10, 30, 50, 70, 90, 120, 160, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1800, 2300, 3000, 4000, 5000 ]

class WhitespaceFraction(FeatureExtractor):
  def Extract(self, post):
    numWhitespace = 0
    i = 0
    while i < len(post.fulltext):
      if string.whitespace.find(post.fulltext[i]) != -1:
        numWhitespace += 1
      i += 1
    return float(numWhitespace)/float(len(post.fulltext))

  nickname = "whitespacefraction"
  discretization = [ 0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.6 ]

class CharactersPerWord(FeatureExtractor):
  def Extract(self, post):
    return float(len(post.fulltext))/float(len(post.words))

  nickname = "charactersperword"
  discretization = [ 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20 ]

class ApostrophesPerWord(FeatureExtractor):
  def Extract(self, post):
    numApostrophes = 0
    for c in post.fulltext:
      if c == "'": numApostrophes += 1
    if len(post.words) > 0:
      return float(numApostrophes)/float(len(post.words))
    else:
      return 0

  nickname = "apostrophesperword"
  discretization = [ 0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.09, 0.1, 0.3 ]

class LetterFrequencies(FeatureExtractor):
  def Extract(self, post, redo):
    if  redo == False:
      return self.letterFreqs
    self.letterFreqs = np.array([0]*26)
    for w in post.words:
      for c in w:
        if string.ascii_lowercase.find(c) != -1:
          self.letterFreqs[ord(c) - ord('a')] += 1
    self.letterFreqs = self.letterFreqs / np.sum(self.letterFreqs)
    return self.letterFreqs

class LetterFrequency_a(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 0

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_a"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_b(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 1

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_b"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_c(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 2

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_c"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_d(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 3

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_d"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_e(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 4

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_e"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_f(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 5

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_f"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_g(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 6

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_g"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_h(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 7

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_h"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_i(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 8

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_i"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_j(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 9

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_j"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_k(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 10

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_k"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_l(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 11

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_l"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_m(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 12

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_m"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_n(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 13

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_n"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_o(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 14

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_o"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_p(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 15

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_p"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_q(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 16

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_q"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_r(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 17

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_r"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_s(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 18

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_s"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_t(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 19

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_t"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_u(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 20

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_u"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_v(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 21

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_v"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_w(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 22

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_w"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_x(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 23

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_x"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_y(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 24

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_y"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

class LetterFrequency_z(FeatureExtractor):

  def __init__(self, lettFreq, redo):
    self._lettFreq = lettFreq
    self._redo = redo
    self._idx = 25

  def Extract(self, post):
    return self._lettFreq.Extract(post, self._redo)[self._idx]

  nickname = "letterfrequency_z"
  discretization = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

# Katherine's additions:
# ------------------------------------------------
class DigitFraction(FeatureExtractor):
# Count what fraction of full text are digits
   def Extract(self, post):
      numDigits = 0
      numLetters = 0
      for c in post.fulltext:
         if string.digits.find(c) != -1:
            numDigits += 1
      if numDigits > 0:
         return float(numDigits)/float(len(post.fulltext))
      else:
         return 0.0

   nickname = "digitfraction"
   discretization = [0, 0.002, 0.004, 0.006, 0.008, 0.01, 0.04, 0.07, 0.1, 0.5]


class PunctuationFraction(FeatureExtractor):
   def Extract(self, post):
      pcount = 0
      for c in post.fulltext:
         if ((c=='.') or (c==';') or (c=='!') or (c=='?') or (c==',')):
            pcount += 1
      if len(post.words) > 0:
         return float(pcount)/float(len(post.fulltext))
      else:
         return 0.0

   nickname = "punctuationfraction"
   discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class SpecialCharFraction(FeatureExtractor):
   def Extract(self, post):
      scount = 0
      for c in post.fulltext:
         if(not(string.ascii_letters or string.digits)):
            if ((c == '~') or (c == '@') or (c == '$') or (c == '%') or (c == '^') or (c == '&') or (c == '*') or (c == '+') or (c == '<') or (c == '>') or (c == '/') or (c == '_') or (c == '#')):
               scount += 1
      if len(post.words)>0:
         return float(scount)/float(len(post.fulltext))
      else:
         return 0.0

   nickname = "specialcharfraction"
   discretization = [0, 0.001, 0.003, 0.005, 0.007, 0.01, 0.03, 0.05, 0.1]

class EmoticonsFraction(FeatureExtractor):
   def Extract(self,post):
      ecount = 0
      ind = 0
      length = len(post.fulltext)
      for c in post.fulltext:
         ind+=1
         # emoticons with eyes and mouth only
         if((c == ':') or (c == ';') or (c == '=')): 
            if(ind < length):
               nextChar = post.fulltext[ind]
               # nose and mouth
               if(nextChar == '-'):
                  if((ind+1) < length):
                      nextnextChar = post.fulltext[ind+1]
                      if((nextnextChar  == ')') or (nextnextChar == 'D') or (nextnextChar == '(') or (nextnextChar == 'S') or (nextnextChar == 'P') or (nextnextChar == 'o')):
                         ecount += 1
               # no nose, only mouth
               if((nextChar  == ')') or (nextChar == 'D') or (nextChar == '(') or (nextChar == 'S') or (nextChar == 'P') or (nextChar == 'o')):
                  ecount += 1
      if len(post.words) > 0:
         return float(ecount)/float(len(post.fulltext))

   nickname = "emoticonsfraction"
   discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph(FeatureExtractor):
   # For all words in the document, enumerate the number of bigrams.
   # Then divide by the total number of words in the document
   buckets = None
   def Extract(self, post, redo):
      if (redo == False):
        return self.buckets
      self.buckets = [[0 for col in range(26)] for row in range(26)]     
      for w in post.words:
         length = len(w)
         ind = 0
         for c in w:
            if(ind < (length-1)):
               currentChar = c
               nextChar = post.fulltext[ind+1]
               if((string.ascii_letters.find(currentChar) != -1)  and (string.ascii_letters.find(nextChar) != -1)):
                  valueCurrent = ord(currentChar.lower()) - ord('a')
                  valueNextChar = ord(nextChar.lower()) - ord('a')
                  self.buckets[valueCurrent][valueNextChar] += 1
            ind += 1

      # divide by number of words in document:
      numWords = len(post.words)
      if numWords > 0:
         for i in range(0,26):
            for j in range(0,26):
               self.buckets[i][j] = float(self.buckets[i][j]) / float(numWords) 
               
      
      # print out results
      #file = open("name_52_1088.txt", "w")
      #i = 0
      #for arr in buckets:
      #  firstletter = string.ascii_lowercase[i]
      #  j = 0
      #  for val in arr:
      #    secondletter = string.ascii_lowercase[j]
      #    j += 1
      #    file.write(str(val) + "\n")          
          #file.write(firstletter + secondletter + " " + str(val) + "\n")
      #  i += 1
      #file.close()
      
      return self.buckets
     
   nickname = "bigraph"
   discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]    

class Bigraph_aa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_aa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ab(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ab"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ac(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ac"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ad(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ad"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ae(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ae"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_af(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_af"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ag(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ag"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ah(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ah"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ai(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ai"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_aj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_aj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ak(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ak"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_al(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_al"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_am(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_am"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_an(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_an"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ao(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ao"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ap(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ap"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_aq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_aq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ar(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ar"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_as(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_as"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_at(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_at"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_au(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_au"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_av(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_av"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_aw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_aw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ax(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ax"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ay(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ay"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_az(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 0
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_az"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ba(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ba"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_be(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_be"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_br(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_br"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_by(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_by"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_bz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 1
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_bz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ca(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ca"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ce(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ce"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ch(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ch"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ci(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ci"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ck(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ck"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_co(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_co"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ct(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ct"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_cz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 2
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_cz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_da(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_da"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_db(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_db"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_de(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_de"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_df(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_df"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_di(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_di"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_do(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_do"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ds(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ds"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_du(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_du"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_dz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 3
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_dz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ea(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ea"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_eb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_eb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ec(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ec"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ed(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ed"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ee(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ee"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ef(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ef"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_eg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_eg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_eh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_eh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ei(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ei"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ej(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ej"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ek(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ek"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_el(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_el"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_em(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_em"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_en(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_en"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_eo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_eo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ep(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ep"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_eq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_eq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_er(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_er"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_es(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_es"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_et(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_et"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_eu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_eu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ev(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ev"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ew(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ew"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ex(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ex"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ey(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ey"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ez(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 4
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ez"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fe(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fe"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ff(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ff"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ft(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ft"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_fz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 5
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_fz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ga(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ga"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ge(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ge"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_go(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_go"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_gz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 6
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_gz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ha(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ha"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_he(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_he"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ho(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ho"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ht(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ht"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_hz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 7
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_hz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ia(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ia"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ib(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ib"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ic(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ic"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_id(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_id"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ie(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ie"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_if(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_if"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ig(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ig"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ih(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ih"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ii(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ii"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ij(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ij"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ik(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ik"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_il(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_il"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_im(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_im"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_in(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_in"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_io(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_io"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ip(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ip"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_iq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_iq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ir(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ir"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_is(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_is"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_it(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_it"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_iu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_iu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_iv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_iv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_iw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_iw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ix(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ix"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_iy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_iy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_iz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 8
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_iz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ja(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ja"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_je(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_je"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ji(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ji"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_js(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_js"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ju(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ju"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_jz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 9
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_jz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ka(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ka"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ke(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ke"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ki(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ki"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_km(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_km"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ko(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ko"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ks(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ks"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ku(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ku"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ky(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ky"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_kz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 10
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_kz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_la(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_la"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ld(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ld"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_le(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_le"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_li(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_li"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ll(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ll"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ln(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ln"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ls(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ls"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ly(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ly"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_lz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 11
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_lz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ma(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ma"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_md(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_md"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_me(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_me"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ml(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ml"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ms(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ms"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_my(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_my"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_mz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 12
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_mz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_na(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_na"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ne(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ne"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ng(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ng"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ni(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ni"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_no(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_no"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_np(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_np"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ns(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ns"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ny(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ny"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_nz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 13
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_nz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ob(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ob"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_od(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_od"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oe(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oe"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_of(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_of"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_og(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_og"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ok(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ok"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ol(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ol"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_om(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_om"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_on(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_on"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_op(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_op"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_or(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_or"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_os(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_os"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ot(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ot"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ou(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ou"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ov(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ov"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ow(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ow"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ox(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ox"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_oz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 14
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_oz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pe(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pe"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ph(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ph"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_po(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_po"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ps(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ps"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_px(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_px"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_py(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_py"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_pz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 15
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_pz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qe(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qe"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ql(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ql"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_qz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 16
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_qz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ra(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ra"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_re(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_re"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ri(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ri"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ro(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ro"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ru(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ru"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ry(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ry"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_rz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 17
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_rz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_se(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_se"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_si(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_si"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_so(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_so"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ss(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ss"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_st(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_st"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_su(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_su"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_sz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 18
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_sz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ta(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ta"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_td(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_td"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_te(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_te"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_th(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_th"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ti(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ti"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_to(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_to"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ts(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ts"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ty(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ty"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_tz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 19
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_tz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ua(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ua"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ub(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ub"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ud(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ud"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ue(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ue"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ug(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ug"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ui(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ui"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ul(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ul"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_um(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_um"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_un(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_un"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_up(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_up"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ur(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ur"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_us(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_us"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ut(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ut"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ux(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ux"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_uz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 20
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_uz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_va(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_va"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ve(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ve"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_vz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 21
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_vz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_we(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_we"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ws(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ws"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ww(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ww"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_wz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 22
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_wz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xa(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xa"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xe(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xe"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_xz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 23
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_xz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ya(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ya"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ye(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ye"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ym(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ym"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ys(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ys"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_yz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 24
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_yz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_za(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 0

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_za"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zb(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 1

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zb"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zc(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 2

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zc"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zd(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 3

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zd"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_ze(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 4

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_ze"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zf(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 5

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zf"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zg(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 6

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zg"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zh(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 7

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zh"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zi(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 8

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zi"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zj(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 9

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zj"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zk(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 10

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zk"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zl(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 11

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zl"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zm(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 12

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zm"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zn(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 13

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zn"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zo(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 14

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zo"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zp(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 15

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zp"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zq(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 16

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zq"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zr(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 17

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zr"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zs(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 18

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zs"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zt(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 19

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zt"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zu(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 20

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zu"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zv(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 21

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zv"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zw(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 22

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zw"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zx(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 23

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zx"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zy(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 24

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zy"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

class Bigraph_zz(FeatureExtractor):

  def __init__(self, bigraph, redo):
    self._bigraph = bigraph
    self._redo = redo
    self._firstIdx = 25
    self._secondIdx = 25

  def Extract(self, post):
    return self._bigraph.Extract(post, self._redo)[self._firstIdx][self._secondIdx]

  nickname = "bigraph_zz"
  discretization = [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.3]

