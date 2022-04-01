with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    data = []
    ip_db = {}
    for line in f:
        line = line.split()
        data.append((line[0], line[5].replace('"', ''), line[6]))
    for line in data:
        ip_db[line[0]] = ip_db.get(line[0], 0) + 1



print(*data, sep="\n")
spamer = max(ip_db.items(), key=lambda i: i[1])
print(f"IP адрес спамера: {spamer[0]} количество запросов: {spamer[1]}")

