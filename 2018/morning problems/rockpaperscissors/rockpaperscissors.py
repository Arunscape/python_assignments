num_matches = int(input())
awonm=0
bwonm=0
for i in range(num_matches):
    rounds = input().split()
    # now rounds is a list of the rounds in this match
    # example: if the line of input was "RR RP SR" then
    # rounds == ["RR", "RP", "SR"]
    # now do the rest!
    awonr=0
    bwonr=0
    for j in rounds:
        if j[0] == 'R':
            if j[1] == 'R':
                pass
            elif j[1] == 'P':
                bwonr+=1
            elif j[1] == 'S':
                awonr+=1

        elif j[0] == 'P':
            if j[1] == 'P':
                pass
            elif j[1] == 'S':
                bwonr+=1
            elif j[1] == 'R':
                awonr+=1

        elif j[0] == 'S':
            if j[1] == 'S':
                pass
            elif j[1] == 'R':
                bwonr+=1
            elif j[1] == 'P':
                awonr+=1


    if awonr > bwonr:
        awonm+=1
    elif bwonr > awonr:
        bwonm+=1
# print here whoever is the overall winner of all the matches and
# how many matches the winner won
if awonm >= bwonm:
    print('Alice {}'.format(awonm))
else:
    print('Bob {}'.format(bwonm))
