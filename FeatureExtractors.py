import string
import copy

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
