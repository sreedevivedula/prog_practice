if __name__ == "__main__":
    n = input()
    strList = []
    for i in range(0,n):
        strList.append(raw_input())
    q = input()
    queryList = []
    for i in range(0,q):
        queryList.append(raw_input())

    strListSorted = sorted(strList)
    
    for q in queryList:
        print(strList.count(q))
