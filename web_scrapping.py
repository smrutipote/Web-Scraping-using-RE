import re                                                        #for Regular Expression
import urllib
import pandas as pd


from urllib.request import urlopen

url='https://www.contactlistpro.com/contact-list/3-columns/'

data = urlopen(url)                                               #used to open url
data= data.read().decode()                                        #used to read and convert html data
data= re.sub('/+?.<>\n', '',data)
data= re.sub('>',' ',data)
data= re.sub('<',' ',data)                                        #removing characters and symbols
#print(data)

#Extracting contact numbers from data
tel_number= re.findall('(tel:[0-9]{10})',data)
tel_number= " ". join(tel_number)
tel_numer= re.sub('tel:','', tel_number)
tel_numer = tel_numer.split(' ')             
del(tel_numer[-2:])                                               #removing unnecessary data
print(len(tel_numer),tel_numer)

#Extracting city names from data
city = re.findall('[a-zA-Z]{1,20}[,]\s[a-zA-Z]{1,20}[,]\s[a-zA-Z]{1,20}', data)
print(len(city),city)

#Extracting names from data
names = re.findall('[A-Z][a-z]{1,20}\s[A-Z][a-z]{1,20}\s/div', data)
names = ''.join(names)
name= re.sub(' /div','  ',names)
name = name.split('  ')
del(name[-3:])
print(len(name), name)

#creating dictionary to store all extracted data
dict1= {'Name':name, "Contact":tel_numer,"City":city}

#Into DataFrame
df = pd.DataFrame(dict1, columns=dict1.keys())                         #creating dataframe
print(df)

#To csv
df.to_csv('output_csv', index= False)