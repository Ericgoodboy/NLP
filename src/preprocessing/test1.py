import jieba
import pandas
import os
csvPath = os.path.join("../../","data/neg.csv")

data = pandas.read_csv(csvPath)[0:100]
print(data[:10])
