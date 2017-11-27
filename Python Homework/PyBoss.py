import pandas as pd

myinput = input("What is the employe.csv input file path? :")
outputfile= input("What should be your output file name and desire output file path ?:")

myempfile = myinput
myoutempfile = outputfile

#myempfile='C:\Pri doc\priti\Projects\Myproject\Berkely\Week 3 Python\Homework python\Myboss\employee_data1.csv'
#myoutempfile ='C:\Pri doc\priti\Projects\Myproject\Berkely\Week 3 Python\Homework python\Myboss\empnew1.csv'
#open file

#data= pd.read_csv('C:\Pri doc\priti\Projects\Myproject\Berkely\Week 3 Python\Homework python\Myboss\\employee_data1.csv',parse_dates= [2])


def result(myinfile,myoutfile):
    #data= pd.read_csv('C:\Pri doc\priti\Projects\Myproject\Berkely\Week 3 Python\Homework python\Myboss\employee_data1.csv',parse_dates= [2])
    data= pd.read_csv(myinfile,parse_dates= [2])
    #split name is first and last  name
    data[['FirstName','LastName']] = data['Name'].str.split(' ',expand=True)
    #change the DOB date format
    data['DOB'] = data['DOB'].dt.strftime('%d/%m/%Y')
    #change the state abrrivation
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
    data['State'].replace( us_state_abbrev,inplace=True)
    #Hide first 5 character for SSN 
    data.SSN=data.SSN.str.slice_replace(0,6, "***-**" )
    print(data)
    #update new column in new csv file
    print("My output file need to be ",myoutfile)
    data.to_csv(myoutfile,index=False, sep=',', encoding='utf-8',header=True , columns=["Emp ID","FirstName","LastName","DOB","SSN","State"])


result(myempfile,myoutempfile)