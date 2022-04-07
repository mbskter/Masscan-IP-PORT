# #coding:utf-8

masscantxt = input("请输入masscan的扫描结果:")
masscanfile = open(masscantxt, "r")
masscanfile.seek(0)
for line in masscanfile:
    if line.startswith("#"):
        continue
    if line.startswith("open"):
        line = line.split(" ")
        print(line[3]+":"+line[2])
        with open("masscanconvert.txt", "a") as f:
            f.write(line[3]+":"+line[2]+"\n")
            f.close()
masscanfile.close()
