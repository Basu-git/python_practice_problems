import time
ttime=int(input())
for i in range(ttime,0,-1):
    seconds=i%60
    min=int(i/60)%60
    hours=int(i/3600)%24
    print(f'{hours}:{min:}:{seconds}')
    time.sleep(1)
print("Time Up!!!")
    