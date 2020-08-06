#! python3

import re, pyperclip
#create a regex object for phone numbers
re.compile(r'''
# basic 10 digit phone number witih dashes
# no area code
# area code in parens
# number with ext, or ext. or x followed by up to 5 numbers
(
((\d\d\d) | (\(\d\d\d))))?            # area code (optional)
()\s|-)            # first separator
\d\d\d            # first 3 digits
-                    #separator
\d\d\d\d            # last 4 digits
(()(ext(\.)?\s) | x)        # extension word part (optional)
(\d{2,5}))?           # extension nums (optional)
)
''', re.VERBOSE)
#create a regex object for email addresses
emailRegex = re.compile('''
# som.eth+_ing@someth.ing.edu.gov

[a-zA-Z0-9_.+]+      #before the at
@                     #at symbol
[a-zA-Z0-9_.+]+     #domain name part, including dots!


''', re.VERBOSE)

#get text off clipboard
text = pyperclip.paste()
#extract the email and phone nums from the text
extractedPhones = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhones:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmails)

#copy the extracted emails and phones to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmails)
#could format differently, like by using a comma instead of a new line
pyperclip.copy(results)
