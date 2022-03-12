import json
def save_firebase():
	import firebase_admin
	a = open('electionvnps-firebase-adminsdk-3ypv5-52c9b529b4.json')
	cred_obj = firebase_admin.credentials.Certificate('electionvnps-firebase-adminsdk-3ypv5-52c9b529b4.json')
	default_app = firebase_admin.initialize_app(cred_obj, {
		'databaseURL':'https://electionvnps-default-rtdb.asia-southeast1.firebasedatabase.app/'
		})

def definedict():
	database = {
		'maleSPL': {},
		'femaleSPL': {},
		'maleASPL': {},
		'femaleASPL': {},
		'maleCHERA': {},
		'femaleCHERA': {},
		'maleCHOLA': {},
		'femaleCHOLA': {},
		'malePANDYA': {},
		'femalePANDYA': {},
		'malePALLAVA': {},
		'femalePALLAVA': {},
		'maleCulturalSEC': {},
		'femaleCulturalSEC': {},
		'SwachBarathCoord': {}
	}

	def addkey(n, poststr):
		for i in range(1, n + 1):
			name = input(f'Enter name of Candidate{i}: ')
			database[poststr][f'candidate{i}'] = {'name': name, 'votes': 0}
	n1 = int(input('Enter no of male candidates[for SPL]: '))
	addkey(n1, 'maleSPL')
	n2 = int(input('Enter no of female candidates[for SPL]: '))
	addkey(n2, 'femaleSPL')
	n3 = int(input('Enter no of male candidates[for ASPL]: '))
	addkey(n3, 'maleASPL')
	n4 = int(input('Enter no of female candidates[for ASPL]: '))
	addkey(n4, 'femaleASPL')
	n5 = int(input('Enter no of male candidates[for CHERA]: '))
	addkey(n5, 'maleCHERA')
	n6 = int(input('Enter no of female candidates[for CHERA]: '))
	addkey(n6, 'femaleCHERA')
	n7 = int(input('Enter no of male candidates[for CHOLA]: '))
	addkey(n7, 'maleCHOLA')
	n8 = int(input('Enter no of female candidates[for CHOLA]: '))
	addkey(n8, 'femaleCHOLA')
	n9 = int(input('Enter no of male candidates[for PANDYA]: '))
	addkey(n9, 'malePANDYA')
	n10 = int(input('Enter no of female candidates[for PANDYA]: '))
	addkey(n10, 'femalePANDYA')
	n11 = int(input('Enter no of male candidates[for PALLAVA]: '))
	addkey(n11, 'malePALLAVA')
	n12 = int(input('Enter no of female candidates[for PALLAVA]: '))
	addkey(n12, 'femalePALLAVA')
	n13 = int(input('Enter no of male candidates[for CULTURAL SECRETARY]: '))
	addkey(n13, 'maleCulturalSEC')
	n14 = int(input('Enter no of female candidates[for CULTURAL SECRETARY]: '))
	addkey(n14, 'femaleCulturalSEC')
	n15 = int(input('Enter no of candidate [for Swachh Barath Coordinator]: '))
	addkey(n15, 'SwachBarathCoord')

	f = open('data.json', 'w')
	json.dump(database,f, indent=4)
	f.close()

if __name__ == '__main__':
    definedict()