from tkinter import * 

root = Tk()

fname = input('What is your first name? ')
lname = input('What is your first name? ')
age = input('What is your first name? ')
pincode = input('What is your first name? ')
covtest = 0
covtest2 = 0

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
if nxt == '0:
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

if covtest =0:
	if covtest2 = 0:
		print('Get tested immediately!')
	else:
		print('You should probably get tested!')
