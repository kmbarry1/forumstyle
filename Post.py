class Post:
  # Members:
  #   words (a list of the words in the post)
  #   fulltext (the complete text)
  #   date (e.g. "Sat Mar 31, 2012")
  #   time (minutes since midnight, 0 to 1439)

  def __init__(self, posttext):
    lines = posttext.split('\n')
    self.fulltext = posttext[len(lines[0])+1:]
    line1 = lines[0]
    line1 = line1.split(' ')
    self.date = line1[1]+' '+line1[2]+' '+line1[3]+' '+line1[4]

    # Time is stored as number of minutes since midnight
    # i.e. 12:00 am = 0, 1:11 pm = 791, etc.
    hour = int(line1[5].split(':')[0])
    if hour == 12:
      hour = 0
    min = int(line1[5].split(':')[1])
    self.time = hour*60 + min
    if line1[6][0] == 'p':
      self.time += 12*60

    # Now I want to split the post up into an array of words in a reasonable fashion
    # For the moment, I'm going with a conservative technique...split on spaces,
    # after first inserting them after '.' and '/' characters. This bungles web addresses,
    # and may miss other things, too. '\n' is replaced with ' '.
    # Then all punctuation is removed from the words, and they are lower-cased
    # Right now, any words that were pure punctuation result in empty words, which 
    # are removed.

    import re
    import string
    spacedtext = re.sub('\.', '\. ', self.fulltext)
    spacedtext = re.sub('/', '/ ', spacedtext)
    spacedtext = re.sub('\\n', ' ', spacedtext)
    spacedtext = re.sub('\\?', ' ', spacedtext)
    self.words = spacedtext.split(' ')
    nWords = len(self.words)
    i = 0
    while i < nWords:
      w = self.words[i].lower()
      cleanw = ''
      nChars = len(w)
      j = 0
      while j < nChars:
        if string.ascii_lowercase.find(w[j]) != -1:
          cleanw = cleanw + w[j]
        j += 1
      self.words[i] = cleanw
      i += 1
    i = 0
    while i != len(self.words):
      if len(self.words[i]) == 0:
        del self.words[i]
        i -= 1
      i += 1
