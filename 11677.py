from datetime import datetime, timedelta, time


def main():
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        return
    t1 = datetime.combine(datetime.today(), time(H1, M1))
    t2 = datetime.combine(datetime.today(), time(H2, M2))
    if t2 < t1:
        t2 += timedelta(days=1)
    delta = t2 - t1
    minutes = delta.total_seconds() / 60
    print(int(minutes))


while True:
    try:
        main()
    except EOFError:
        break
