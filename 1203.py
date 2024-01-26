def main():
    register = []
    reg = input()
    while reg != "#":
        _, q, p = reg.split()
        item = {"q": int(q), "time_interval": int(p), "exec_time": int(p)}
        register.append(item)
        reg = input()
    k = int(input())
    register.sort(key=lambda x: x["q"])
    while k > 0:
        min_time = register[0]["exec_time"]
        for i in range(len(register)):
            if register[i]["exec_time"] < min_time:
                min_time = register[i]["exec_time"]
        for i in range(len(register)):
            if register[i]["exec_time"] == min_time:
                register[i]["exec_time"] += register[i]["time_interval"]
                print(register[i]["q"])
                k -= 1


while True:
    try:
        main()
    except EOFError:
        break
