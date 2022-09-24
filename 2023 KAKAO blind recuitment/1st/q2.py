# %%
def solution(cap, n, deliveries, pickups):
    lastIDelv = max(filter(lambda e: e[1] > 0, enumerate(deliveries)), key=lambda e:e[0], default=[-2])[0]+1
    lastIPick = max(filter(lambda e: e[1] > 0, enumerate(pickups)), key=lambda e:e[0], default=[-2])[0]+1
    # # 
    count = 0
    while not(lastIDelv ==-1 and lastIPick == -1):
        # 
        count += max(lastIDelv, lastIPick) * 2
        # 
        sendPayload=cap
        for i in reversed(range(-1, lastIDelv)):
            if i == -1:
                lastIDelv = -1
                break
            sendDelv = min(sendPayload, deliveries[i])
            deliveries[i] -= sendDelv
            sendPayload -= sendDelv
            if sendPayload ==0:
                lastIDelv = i+1
                if deliveries[i] != 0:
                    break
        # 
        recvPayload=cap
        for i in reversed(range(-1, lastIPick)):
            if i == -1:
                lastIPick = -1
                break
            recvDelv = min(recvPayload, pickups[i])
            pickups[i] -= recvDelv
            recvPayload -= recvDelv
            if recvPayload == 0:
                lastIPick = i+1
                if pickups[i] != 0:
                    break

        
    
    return count


solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
