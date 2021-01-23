from tkinter import *
from sqlite3 import *

root = Tk()
connection = sqlite3.connect("covid19")
cursor = connection.cursor()

cont = input('Do you want to edit an existing profile?(1 for yes, 0 for no) ')
if cont == 1:
	fna = input('What is the first name of the profile? ')
	lna = input('What is the second name of the profile? ')
	passw = input('What is your password? ')
	name = fna+lna
	rows = cursor.execute(
		"SELECT password FROM corona WHERE password = ?",
		(pass,),
	).fetchall()
	if len(rows<0):
		virus = input('type covid state to alter your c`ovid state, Malayria state for your malayria state, and Cholera state for your cholera state')
		newstatus = input(' type yes if you want to update the profile to having the diease and no for the opposite ')
		cursor.execute(
			"UPDATE corona SET ? = ? WHERE pssword = ?",
			(virus, newstatus, passw)
		)
	else:
		print('wrong password')



fname = input('What is your first name? ')
lname = input('What is your first name? ')
age = input('What is your first name? ')
pincode = input('What is your first name? ')
passw = input('what would you like your password to be? ')

covtest = 0
covtest2 = 0
maltest = 0
choltest = 0

print('difficulty breathing or shortness of breath')
print('chest pain or pressure')
print('loss of speech or movement')
print('aches and pains')
print('sore throat')
print('diarrhoea')
print('conjunctivitis')
print('headache')
print('loss of taste or smell')
print('A rash on skin, or discolouration of fingers or toes')
print('fever')
print('dry cough')
print('tiredness')
nxt = input('Do you experience any of the above?(1 for yes, 0 for no)')
if nxt == '0':
	covtest2+=1

temp = input('What is your temperature(Use a thermometer)? ')
Bp = input('What is your diastolic blood pressure(A sphygmomanometer can be used)? ')
O2 = input('what is your oxygen level(An electronic oxygen measuring device can be used)? ')
Eg = input('Does you ECG test give you any problems(ECG = electrocardiogram test 0 for yes 1 for no)? ')

if int(temp)>96 and int(temp)<99:
	covtest+=1

if int(Bp) BP <90:
	covtest+=1
	
if int(O2) >89 and int(O2) <93:
	covtest +=1

if Eg == '1':
	covtest +=1

if covtest == 0:
	if covtest2 == 0:
		print('Get tested immediately!')
	else:
		print('You should probably get tested for coronavirus!')
if covtest2 == 0:
	print('Get test for coronavirus.')

if covtest2 == 0:
	print('Pain in abdomen/muscles')
	print('chills')
	print('fatigue')
	print('fever')
	print('night sweats')
	print('shivering')
	print('sweating')
	print('diarrhoea')
	print('nausea')
	print('vomiting')
	print('fast heart rate')
	print('headache')
	print('mental confusion')
	print('pallor/paleness')
	nxt = input('Do you experience any of the above?(1 for yes, 0 for no)')
	if nxt == 0:
		maltest += 1

if maltest == 0:
	print('Pain in the abdomen')
	print('nausea')
	print('severe diarrhoea')
	print('vomiting')
	print('watery diarrhoea')
	print('dehydration')
	print('lethargy')
	print('water-electrolyte imbalance')
	nxt = input('Do you experience any of the above?(1 for yes, 0 for no)')
	if nxt == 0:
		choltest += 1
		
cursor.execute("INSERT INTO corona VALUES (?, ?, ?, 'no', 'no', 'no',  ? )"
	      (fname+' ' + lname, age, pincode, passw)
	      )

rows = cursor.execute(
    "SELECT name, age, pincode, covid state, malayria state, cholera state FROM corona WHERE covid state = 'yes' OR malayria state = 'yes' OR cholera statess",
).fetchall()
print(rows)
