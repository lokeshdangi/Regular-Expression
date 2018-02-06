import re

#will compare only at the beginning
x = 'look book pook mook took'
re.match('[a-d]ook',x)

#will compare only at the beginning
x = 'book look pook mook took'
result = re.match('[a-d]ook',x)
print(result.group(0))

#first occurance from start
x = 'look pook book mook took'
result = re.search('[a-d]ook',x)
print(result.group(0))


#first occurance from start (flag = re.I) which is for case insensitive
x = 'look pook Book  mook took'
result = re.search('[a-d]ook',x,re.I)
print(result.group(0))


#finds all occurances in the string
x = 'look pook book mook took'
result = re.findall('[a-r]ook',x)
print(result)



string = input('Enter a string')
#finding digits
d = re.findall('[0-9]',string)
#finding vowels
v = re.findall('[aeiou]',string,re.I)
print(d)
print(v)




x = '123abc'
result = re.sub('[\d]','-',x)
print(result)


x = '2018 is good as compared to 2017'
result = re.sub('[\d]{2}|[aeiou]','-',x,count = 2)
print(result)




p = re.compile('[\d]{10}')
string = input('Enter a mobile number')
result = p.match(string)
if result:
    print('Valid')
else:
    print('Invalid')
    


p = re.compile('^[\d]{10}$')
string = input('Enter a mobile number')
result = p.match(string)
if result:
    print('Valid')
else:
    print('Invalid')'
    



#1
string = input('Enter a string')
result = re.findall('\d',string)
result = list(map(int,result))
print(sum(result))

#2
string =  'i_r there g_o_d k_a_z_b'
result = re.findall('([a-z](_[a-z])+)',string)
for r in result:
    print(r[0])
print(result)

#3
string = 'Lokesh'
result = re.findall('[^A-Z0-9_]|[^a-z0-9_]',string)
if len(result) == len(string):
    print(result)
    print('Valid')
else:
    print('Invalid')

#4
string = '001.108.011.020'
result= re.sub('\.[0]+','.',re.sub('^[0]+','',string))
print(result)

#5
string = '1997-12-02'
year = re.findall('(\d{2,4})-(\d{1,2})-(\d{1,2})',string)
print('{}-{}-{}'.format(year[0][2],year[0][1],year[0][0]))


#6
string = input('Enter a string')
result = re.sub('\s|\,|\.','-',string)
print(result)

#7
string = input('Enter license plate number :')
result = re.search('RJ\s*[0-9]{2}\s*[a-z]{2}\s*[0-9]{4}$',string,re.I)
if result:
    print('Valid')
else:
    print('Invalid')







































