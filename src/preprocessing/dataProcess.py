import jieba
import re
import pandas
import os
import numpy as np
normal = [(0,"<GO>"),(1,"<END>"),(2,"<UNK>")]#固定占位符

normalLen = len(normal)
deleteChar = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")

#加载数据
def loadData(path):
    csvPath = os.path.join(path)
    data = pandas.read_csv(csvPath)[0:10000]
    data =np.array(data)
    data =data.flatten()
    print(data.shape)
    data = [deleteChar.sub("",i) for i in data]
    print(data)
    data = [[j for j in jieba.cut(i)] for i in data]
    print(data)


#词频统计
def countWords(data,maxLen=-1):
    resDic = {}
    for line in data:
        for word in line:
            if word in resDic:
                resDic[word]+=1
            else:
                resDic[word]=1
    resDic = [(i, resDic[i]) for i in resDic]
    resDic.sort(key=lambda x: -x[1])
    if maxLen is not -1:
        resDic =resDic[0:maxLen-normalLen]
    return resDic
#获取id字典
def genIds(resdict):#生成占位符，也就是id
    dictId = []
    i=normalLen
    for d in resdict:
        dictId.append((i,d[0]))
        i+=1
    return normal+dictId
#将词转化为id
def wordToIds(resIds,data):
    resDict={i[1]:i[0]for i in resIds}
    def t(d):
        if d not in resDict:
            d="<UNK>"
        return resDict[d]
    res = [ [0]+[ t(j) for j in i]+[1]for i in data]
    return res
