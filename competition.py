from big_bite import big_bite

contestants = [3,2,1,432,2,32,12,5,3,5]
rank = []

def promote_contestant(contestant):
    global rank
    promoted = False
    for i in range(len(rank)):
        if rank[i] == contestant:
            if i == 0:
                ''' do nothing '''
                promoted = True
            else:
                rank[i-1], rank[i] = rank[i], rank[i-1]
                promoted = True
    if not promoted:
        rank.append(contestant1)

print('Which of the following is better?')
for contestant1, contestant2 in big_bite(itertools.cycle(contestants)):
    print('1. {}'.format(contestant1))
    print('2. {}'.format(contestant2))
    print('3. Quit and exit.')
    while True:
        try:
            answer = int(input())
            if answer not in [1,2,3]:
                raise ValueError
            break
        except ValueError:
            print('Input must be 1, 2, or 3.')
    if answer == 1:
        print('you chose: {}'.format(contestant1))
        # promote contestant1:
        promote_contestant(contestant1)
    elif answer == 2:
        print('you chose: {}'.format(contestant2))
        # promote contestant2:
        promote_contestant(contestant2)
    else:
        print('Winner: {}'.format(rank[0]))
        print (rank)
        exit(0)
