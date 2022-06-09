import json
import time
dataStorage = []

def result(post):
    finalString = ''
    f = open('data.json', 'r')
    data = json.load(f)
    post_dict = data[post]
    post_candidates = data[post].keys()
    votes = []

    for i in post_candidates:
        votes.append(post_dict[i]['votes'])
    try:
        highest = max(votes)
    except ValueError:
        highest = 0
        finalString = f'For {post}, no candidature found!'
        writeResult('arraySave', finalString)
        print(finalString)
        return None
    votesindex = []
    for i in votes:
        if i == highest:
            votesindex.append(votes.index(i))
            votes[votes.index(i)] = 'Counted'
    print(f'Results generated for {post}')
    if len(votesindex) == 1:
        finalString = f'The winner for the {post} post is '+post_dict[f'candidate{votesindex[0] + 1}']['name']+f' with {highest} votes'

    elif len(votesindex) > 1:
        finalString = f'There is a Tiebreaker for the post of {post} between '
        for i in range(len(votesindex)):
            finalString += post_dict[f'candidate{votesindex[i] + 1}']['name']
            if i != len(votesindex)-1:
                finalString += ', '
            else:
                finalString += ' '
        finalString += f'at {highest} votes'
    print(finalString)
    writeResult('arraySave', finalString)
    print('\n\n')

def writeResult(mode, data = None):
    if mode == 'arraySave':
        dataStorage.append(data)
    elif mode == 'diskSave':
        fileHandle = open('Results.txt', 'w')
        for statement in dataStorage:
            fileHandle.write(statement)
            fileHandle.write('\n')
        fileHandle.close()
        print('Data sucessfully saved at Results.txt')

# Function call
result('maleSPL')
result('femaleSPL')
result('maleASPL')
result('femaleASPL')
result('maleCHERA')
result('femaleCHERA')
result('maleCHOLA')
result('femaleCHOLA')
result('malePANDYA')
result('femalePANDYA')
result('malePALLAVA')
result('femalePALLAVA')
result('maleCulturalSEC')
result('femaleCulturalSEC')
result('SwachBarathCoord')

saveQ = int(input('Do you want to save the following data in your computer?\n1: YES\n2: NO\n>>> '))
while saveQ not in [1,2]:
    print('Invalid input, use either 1 or 2.')
    saveQ = int(input('Do you want to save the following data in your computer?\n1: YES\n2: NO\n>>> '))
if saveQ == 1:
    writeResult('diskSave')

time.sleep(5)