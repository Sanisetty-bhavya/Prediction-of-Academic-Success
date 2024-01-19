#Loading data

df = pd.read_csv('projectdata.csv')
df

# Renaming columns

df.columns=["Marital status" ,"Application mode","Application order","Course","Daytime/evening attendance","Previous qualification","Previous qualification (grade)","Nationality","Mothers qualification","Fathers qualification","Mothers occupation","Fathers occupation","Admission grade","Displaced","Educational special needs","Debtor","Tuition fees up to date","Gender","Scholarship holder","Age at enrollment","International","Curricular units 1st sem (credited)","Curricular units 1st sem (enrolled)","Curricular units 1st sem (evaluations)","Curricular units 1st sem (approved)","Curricular units 1st sem (grade)","Curricular units 1st sem (without evaluations)","Curricular units 2nd sem (credited)","Curricular units 2nd sem (enrolled)","Curricular units 2nd sem (evaluations)","Curricular units 2nd sem (approved)","Curricular units 2nd sem (grade)","Curricular units 2nd sem (without evaluations)","Unemployment rate","Inflation rate","GDP","Target"]
df

# Replacing to avoid duplicants

df['Marital status'] = df['Marital status'].replace({' 1': '1', '2 ': '2','3 ': '3','4 ': '4',' 5':'5','6 ':'6'})
df['Application mode'] = df['Application mode'].replace({'1': '1','2': '2','5': '5','7': '7','10': '10','15': '15','16': '16','17': '17','18': '18','26': '26','27': '27','39': '39','42': '42','43': '43','44': '44','51': '51','53': '53','57': '57'})
df['Course'] = df['Course'].replace({'33': '33','171': '171','8014': '8014','9003': '9003','9070': '9070','9085': '9085','9119': '9119','9130': '9130','9147': '9147','9238': '9238','9254': '9254','9500': '9500','9556': '9556','9670': '9670','9773': '9773','9853': '9853','9991': '9991'})
df['Daytime/evening attendance'] = df['Daytime/evening attendance'].replace({'1': '1', '0': '0'})
df['Previous qualification'] = df['Previous qualification'].replace({'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '9': '9', '10': '10', '12': '12', '14': '14', '15': '15', '19': '19', '38': '38', '39': '39', '40': '40', '42': '42', '43': '43'})
df['Nationality'] = df['Nationality'].replace({'1': '1','2': '2','6': '6','11': '11','13': '13','14': '14','17': '17','21': '21','22': '22','24': '24','25': '25','26': '26','32': '32','41': '41','62': '62','100': '100','101': '101','103': '103','105': '105','108': '108','109': '109'})
df['Mothers qualification'] = df['Mothers qualification'].replace({'1 ': '1','2': '2','3': '3','4 ': '4','5 ': '5','6 ': '6','9': '9','10 ': '10','11 ': '11','12 ': '12','14 ': '14','18': '18','19 ': '19','22 ': '22','26': '26','27 ': '27','29 ': '29','30 ': '30','34': '34','35 ': '35','36 ': '36','37 ': '37','38 ': '38','39 ': '39','40 ': '40','41 ': '41','42 ': '42','43 ': '43','44 ': '44'})
df['Fathers qualification'] = df['Fathers qualification'].replace({'1': '1','2': '2','3 ': '3','4 ': '4','5 ': '5','6 ': '6','9 ': '9','10 ': '10','11': '11','12': '12','13': '13','14': '14','18': '18','19': '19','20': '20','22': '22','25': '25','26 ': '26','27 ': '27','29 ': '29','30': '30','31': '31','33': '33','34': '34','35': '35','36 ': '36','37': '37','38': '38','39 ': '39','40': '40','41': '41','42': '42','43': '43','44 ': '44'})
df['Displaced'] = df['Displaced'].replace({'1': '1','0': '0'})
df['Educational special needs'] = df['Educational special needs'].replace({'1': '1','0': '0'})
df['Debtor'] = df['Debtor'].replace({'1': '1','0': '0'})
df['Tuition fees up to date'] = df['Tuition fees up to date'].replace({'1': '1','0': '0'})
df['Gender'] = df['Gender'].replace({'1': '1','0': '0'})
df['Scholarship holder'] = df['Scholarship holder'].replace({'1': '1','0': '0'})
df['International'] = df['International'].replace({'1': '1','0': '0'})

#checking null data

df.isnull().sum()
