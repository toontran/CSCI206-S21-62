import re

regexp = '(a|b)+' # (a|b)+
pattern = re.compile( regexp )
match = pattern.fullmatch( "eeeeeeabeeeeeebabaeeeeaaabbaaaaeeeee" )
if match == None: print("No match found") # this one did not match
else: print(match.group())

match = pattern.fullmatch( "aabbababaa" )
if match == None: print("No match found")
else: print(match.group()) # prints aabbababaa

match = pattern.search( "eeeeeeabeeeeeebabaeeeeaaabbaaaaeeeee" )
if match == None: print("No match found")
else: print(match.group()) # prints ab

matches = pattern.finditer( "eeeeeeabeeeeeebabaeeeeaaabbaaaaeeeee" )
for m in matches:
    print(m.group()) # prints ab and baba and aaabbaaaa

import urllib.request
def readURL(link):
    f = urllib.request.urlopen(link)
    response = f.read()
    return response.decode('utf-8')
#link = "https://en.wikipedia.org/wiki/Reverse_mathematics"
#string = readURL(link)
#print(string)

def printCourseNumbers(string):
    regexp = '[A-Z]{4} \d{3}' # (a|b)+
    pattern = re.compile( regexp )
    matches = pattern.finditer( string )
    for m in matches:
        print(m.group()) # prints ab and baba and aaabbaaaa
   
def printPhoneNumbers(string): 
    regexp = '\d{3}-\d{3}-\d{4}' # (a|b)+
    pattern = re.compile( regexp )
    matches = pattern.finditer( string )
    for m in matches:
        print(m.group()) # prints ab and baba and aaabbaaaa

def printParagraphs(string): 
    regexp = '<p>.*?<\/p>' # (a|b)+
    pattern = re.compile(regexp, flags=re.DOTALL )
    matches = pattern.finditer(string)
    for m in matches:
        print(m.group()) # prints ab and baba and aaabbaaaa

def printParentheticals(string):
    regexp = '<p>.*?<\/p>' # (a|b)+
    pattern = re.compile(regexp, flags=re.DOTALL )
    matches = pattern.finditer(string)
    for m in matches:
        regexp_in = '\(.*?\)' # (a|b)+
        pattern_in = re.compile(regexp, flags=re.DOTALL )
        matches_in = pattern_in.finditer(m.group())
        for m_in in matches_in:
            print(m_in.group()) # prints ab and baba and aaabbaaaa
 


s = readURL("https://coursecatalog.bucknell.edu/collegeofartsandsciencescurricula/areasofstudy/mathematicsmath/") 

#printCourseNumbers(s)

s = readURL("https://www.bucknell.edu/")

#printPhoneNumbers(s)

#printParagraphs(s)

printParentheticals(s)

pattern = re.compile('([a-z]+).([a-z]+)@')
match = pattern.search("asdf.qwer@bucknell.edu")
print(match.groups())
