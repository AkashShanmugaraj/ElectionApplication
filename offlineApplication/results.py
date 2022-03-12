import json
def result(post):
    f = open('data.json', 'r')
    data = json.load(f)
    post_dict = data[post]
    post_candidates = data[post].keys()
    votes = []

    for i in post_candidates:
        votes.append(post_dict[i]['votes'])
    highest = max(votes)

    votesindex = []
    for i in votes:
        if i == highest:
            votesindex.append(votes.index(i))
            votes[votes.index(i)] = 'Counted'
    print(f'Results generated for {post}')
    if len(votesindex) == 1:
        print('The winner for the specified post is: ')
        print("Name: "+ post_dict[f'candidate{votesindex[0] + 1}']['name'])
        print(f'Votes: {highest}')
    elif len(votesindex) > 1:
        print('Tie breaker for:')
        for i in range(len(votesindex)):
            print("Name: "+ post_dict[f'candidate{votesindex[i] + 1}']['name'])
        print(f'Everyone above secured {highest} votes each')

result('femaleSPL')