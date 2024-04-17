n = int(input())

meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))
    
meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
end_meeting = -1 
for a,b in meeting:
    
    if a >= end_meeting:
        count += 1
        end_meeting = b
print(count)