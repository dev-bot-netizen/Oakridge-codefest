from sqlite3 import *

connection = connect("coronavirus")
cursor = connection.cursor()

final = []

def Pincodealgo(pin):
    region = pin // 10000
    trupin = cursor.execute(
        "SELECT name, Pincode FROM corona"
    ).fetchall()
    result = []
    #print(trupin)
    if region == 11:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region == 12 or region ==13:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >13 or region <17:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region == 17:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region == 18 or region == 19:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >19 and region <29:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >29 and region <35:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >35 and region <40:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] / 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >39 and region <45:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >44 and region <50:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >49 and region <54:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >55 and region <60:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >59 and region <65:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >66 and region <70:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >69 and region <75:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >74 and region <78:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region == 78:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region == 79:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    elif region >79 and region <86:
        for entry in trupin:
            if entry[1] == '':
                continue
            if entry[1] // 10000 == region:
                #print(entry)
                result.append(entry)
    return result
                
cont = input('Do you want to edit an existing profile?(1 for yes, 0 for no) ')
if cont =='1':
    fna = input('What is the first name of the profile? ')
    lna = input('What is the second name of the profile? ')
    pincode = int(input('What is the pincode of the profile? '))
    passw = input('What is your Password? ')
    name = fna+lna
    rows = cursor.execute(
        "SELECT * FROM corona WHERE Password = ?",
        (passw,)
    ).fetchall()
    if len(rows)>0:
        virus = input('type Covid state to alter your covid state, Malayria state for your malayria state, and Cholera state for your cholera state: ')
        virus = virus.lower()
        newstatus = input('Type yes if you want to update the profile to having the diease and no for the opposite: ')
        if virus == 'covid state':
            cursor.execute(
                "UPDATE corona SET 'covid state' = ? WHERE password == ?",
                (newstatus, passw),
        )
        elif virus == 'malayria state':
            cursor.execute(
                "UPDATE corona SET 'malayria state' = ? WHERE password == ?",
                (newstatus, passw),
                )
        elif virus == 'cholera state':
            cursor.execute(
                "UPDATE corona SET 'cholera state' = ? WHERE password == ?",
                (newstatus, passw),
        )
    else:
        print('wrong Password')
    
    result = Pincodealgo(pincode)
    rows = cursor.execute(
        "SELECT Name, Age, Pincode, 'covid state', 'malayria state', 'cholera state' FROM corona WHERE 'covid state' = 'yes' OR 'malayria state' = 'yes' OR 'cholera state' = 'yes'",                                                   
    ).fetchall()

    for i in rows:
        if i in result:
            final.append(i)
    if final == []:
        print("\nNo cases in your region. Yay!")
    else:
        print(*final)   
    connection.commit()
    
    exit()
connection.commit()

fname = input('What is your first name? ')
lname = input('What is your last name? ')
age = input('What is your age? ')
pincode = input('What is your pincode? ')
if len(pincode) != 6:
    print('Invalid pincode')
    exit()
pincode = int(pincode)
passw = input('what would you like your Password to be? ')
fullname= fname+lname

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

temp = input('What is your temperature ˚F(Use a thermometer)? ')
Bp = input('What is your diastolic blood pressure(A sphygmomanometer can be used)? ')
O2 = input('what is your oxygen level(An electronic oxygen measuring device can be used)? ')
Eg = input('Does you ECG test give you any problems(ECG = electrocardiogram test 0 for yes 1 for no)? ')

if int(temp)>96 and int(temp)<99:
    covtest+=1

if int(Bp) <90:
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
    if nxt == '0':
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
    if nxt == '0':
        choltest += 1
        
cursor.execute("INSERT INTO corona VALUES (?, ?, ?, 'no', 'no', 'no',  ? )",
          (fullname, age, pincode, passw,),
          )

#print(Pincodealgo(pincode))
result = Pincodealgo(pincode)
rows = cursor.execute(
    "SELECT Name, Age, Pincode, 'covid state', 'malayria state', 'cholera state' FROM corona WHERE 'covid state' = 'yes' OR 'malayria state' = 'yes' OR 'cholera state' = 'yes'",                                                   
).fetchall()

for i in rows:
    if i in result:
        final.append(i)
if final == []:
    print("\nNo cases in your region. Yay!")
else:
    print(*final)   
connection.commit()
