import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObj = phoneNumRegex.search('my number is 404-862-2810')
matchObj.group()
#'404-862-2810'
matchObj.group(1)
#'404'


oldPhoneRegEx = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = oldPhoneRegEx.search('my number is (404) 862-2810')
mo.group()

batRegex = re.compile(r'bat(man|mobile|copter|cave)')
allList = batRegex.findall('''batman has a bunch of cool gear.
his batcave is full of various objects, including the batmobile,
the batcopter, the batcycle, the batamarang, the battalion of
battered batbats''')
print(allList)
#findall does not return a match object, just a list of strings it found

bat2Regex = re.compile(r'bat(wo)?man')
mo = batRegex.search('adventures of batwoman')

batmoreRegex = re.compile('bat(wo)*man')
mo = batRegex.search('hey batwowowowowowowowowowowowoman')

# question mark allows to appear zero or one time.
#star allows to appear any number of times
#plus allows it to appear one or more times.
#you can escape these characters with backslash if you want to actually find them


haRegex = re.compile(r'(Ha){3,5}')
haRegex.search('He said "HaHaHaHa"')
#{3,} means any number >= 3, {,5} means 0-5
#with range, if you do a ? after it its a non-greedy match, vs greedy match without.
#greedy match means it chooses the longest string that matches the pattern, non greedy is shortest/first

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
phoneRegex.search('My numbers are 555-555-5555,333-3333,999-999-9999')

#digit character class
r'\d' == r'(0|1|2|3|4|5|6|7|8|9)'

#other character classes:
#\D is NOT a digit
#\w is a letter, numeric digit, or underscore character
#\W is any character that is not a letter, digit, or underscore
#\s is a space, tab or new line
#\S is NOT a space, tab or new line

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping,
    9 ladies dancing, 8 maids a milking, 7 swans a swimming 6 geese a laying,
    5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, 1 partridge'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]')
lowerCaseRegex = re.compile(r'[a-z]')
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
notVowelRegex = re.compile(r'^[aeiouAEIOU]') #this does mean any chars, not just consonants

beginsWithHelloRegex = re.compile(r'^Hello') #carat here means must be at start of string
beginsWithHelloRegex.search('Hello there') #it will find it
beginsWithHelloRegex.search('he said "Hello!"') #no finds, returns None
endsWithWorldRegex = re.compile(r'world!$') #$ means at end of string
endsWithWorldRegex.search('hello world!') #yes it will finds
endsWithWorldRegex.search('world! thats what it is')#no find in this one

allDigitsRegex = re.compile(r'^\d+$') #whole text must only be digits, it will greedily give u all

#period character means anything can go there except a new line

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat')
#return value is ['cat', 'hat', 'sat', 'lat', 'mat']

#dot star (.*) means anything any number

string = 'First Name: Zach Last Name: Monteith'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameTup = nameRegex.findall(string)
print("Hello " + nameTup[0][0] + ", or should I say " + nameTup[0][1])

#non greedy dot star with question mark

serve = '<To serve humans> for dinner!!!>'

nongreedy = re.compile(r'<(.*?)>')
greedy = re.compile(r'<(.*)>')
nongreedy.findall(serve) #['To serve humans']
greedy.findall(serve) #['To serve humans> for dinner!!!']

#if you want dot star to include new lines, do this:
dotStar = re.compile(r'.*', re.DOTALL)
#now it really includes EVERYTHING

#ignoring case:
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
vowelRegex = re.compile(r'[aeiou]', re.I) #same thing

agentRegex = re.compile(r'Agent \w+')
agentRegex.findall('Agent Stinko gave the dossier to Agent Blinko')
#['Agent Stinko', 'Agent Blinko']
agentRegex.sub('REDACTED', 'Agent Stinko gave the dossier to Agent Blinko')
#'REDACTED gave the secret documents to REDACTED'

#more sophisticated approach
namesRegex = re.compile(r'Agent (\w)\w+')
namesRegex.findall('Agent Stinko gave the dossier to Agent Blinko')
#['A', 'B']
namesRegex.sub(r'Agent \1***', 'Agent Stinko gave the dossier to Agent Blinko')
#'Agent S*** gave the dossier to Agent B***''


#verbose
re.compile(r'''
(\d\d\d-)|    #area code (without parens) OR
(\(\d\d\d\) )  #area code WITH parens, no dash
\d\d\d    #first 3 digits
-         #second dash
\d\d\d\d  #last 4 digits
\sx\d{2,4}  # extension, like x1234''', re.VERBOSE | re.IGNORECASE | re.DOTALL)
#bitwise operator, makes it so that all the arguments are valid and get put in.
#its a bit old fashioned and doesn't really match other python syntax
