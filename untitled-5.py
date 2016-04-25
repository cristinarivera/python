english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

#def date_converter():

b = '5/11/2012'
first = b.find('/')
second = b.find('/',first+1)
month = b[:first]
day = b[first + 1 : second]
year = b[second + 1:]
print day
print month
print year

m = int(month)
mm = english.find(m)
start_quote = english.find('"',mm)
end_quote = english.find('"',start_quote + 1)
month_english=english[start_quote + 1 : end_quote]
print month_english


#print date_converter(english, '5/11/2012')
#>>> 11 May 2012