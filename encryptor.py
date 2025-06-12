inFp, outFp = None, None
inStr, outStr = "", ""
secu = 0

inFname = input("입력 파일명을 입력하세요: ")
outFname = input("출력 파일명을 입력하세요: ")
mode = input("암호화는 e, 해독은 d를 입력하세요: ")

if mode == 'e':
    secu = 100
elif mode == 'd':
    secu = -100

inFp = open(inFname, "r", encoding="utf-8")
outFp = open(outFname, "w", encoding="utf-8")

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ""
    for ch in inStr:
        chNum = ord(ch)
        chNum = chNum + secu
        outStr = outStr + chr(chNum)

    outFp.write(outStr)

inFp.close()
outFp.close()

print(inFname + " → " + outFname + " 작업 완료")
