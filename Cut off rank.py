def countLevelUpPlayers(cutOffRank, num, scores):                    
    sortedS = sorted(scores, reverse = 1)
    rank = []
    r = 0
    
    for i in range(len(sortedS)):
        if i == 0:
            r += 1
            rank.append(r)
        else:
            if sortedS[i] == sortedS[i-1]:
                rank.append(r)
            else:
                r = i+1
                rank.append(r)
    
    count = 0
    for j in rank:
        if j <= cutOffRank:
            count+=1
        else:
            break
    
    # return [rank, count]
    return count
