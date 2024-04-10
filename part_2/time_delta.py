from datetime import datetime

format = "%a %d %b %Y %H:%M:%S %z"  #Sun 10 May 2015 13:54:36 -0700

for _ in range(int(input())):
    t1 = input()
    t2 = input()
    time1 = datetime.strptime(t1, format)
    time2 = datetime.strptime(t2, format)
    seconds = time1 - time2
    ans = seconds.total_seconds()
    print(abs(int(ans)))