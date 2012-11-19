import Post
import FeatureExtractors as FE
import os

user = os.listdir("../Data")[52]

f = open("../Data/"+user+"/1088.txt")
posttext = f.read()
f.close()

post = Post.Post(posttext)
#print(post.date)
#print(post.time)
#print(post.words)
#print(post.fulltext)

nWords = FE.NumberOfWords()
print("Number of Words: "+str(nWords.Extract(post)))

complexity = FE.Complexity()
print("Complexity: "+str(complexity.Extract(post)))

lettFrac = FE.LetterFraction()
print("Letter Fraction: "+str(lettFrac.Extract(post)))

upperFrac = FE.UppercaseFraction()
print("Uppercase Fraction: "+str(upperFrac.Extract(post)))

time = FE.TimeOfPosting()
print("Time of Posting: "+str(time.Extract(post)))

numChar = FE.NumberOfCharacters()
print("Number of Characters: "+str(numChar.Extract(post)))

fracWhite = FE.WhitespaceFraction()
print("Fraction of Whitespace Characters: "+str(fracWhite.Extract(post)))

charPerWord = FE.CharactersPerWord()
print("Characters Per Word: "+str(charPerWord.Extract(post)))

aposPerWord = FE.ApostrophesPerWord()
print("Apostrophes Per Word: "+str(aposPerWord.Extract(post)))
