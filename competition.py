import itertools
from big_bite import big_bite

contestants = [5,4,2,3,1]

def promote_contestant(contestant, rank):
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
        rank.append(contestant)

def compete(contestants):
    rank = []
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
            promote_contestant(contestant1, rank)
        elif answer == 2:
            print('you chose: {}'.format(contestant2))
            # promote contestant2:
            promote_contestant(contestant2, rank)
        else:
            print('Winner: {}'.format(rank[0]))
            print (rank)
            exit(0)

if __name__ == '__main__':
    compete(contestants)
