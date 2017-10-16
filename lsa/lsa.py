import sklearn
import json
from pathlib import Path
import re
import string

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans
import pandas as pd
import warnings
import numpy as np

# Suppress warnings from pandas library
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pandas", lineno=570)


with Path('../data/realCaseLinks.txt').resolve().open('r') as fi:
    dataList = [line.split(',') for line in fi.read().strip().split('\n')]



path = Path('/home/daniel/Downloads/hackgt/CourtListener/opinions/').resolve()
datas = []
files = []
names = []

counter = 0

for fil in dataList:
    for p in path.iterdir():
        if (p / fil[0]).is_file():
            f = p / fil[0]

    r = f.open('r')
    data = json.loads(r.read())
    r.close()

    s = data['plain_text']
    s = re.sub('\s+', ' ', s)
    s = s.strip()

    files.append(str(f))
    datas.append(s)
    names.append(fil[2] + ' -- ' + fil[1])

print('Finished parsing {} files'.format(len(datas)))

vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=500, stop_words='english')
dtm = vectorizer.fit_transform(datas)

print(vectorizer.get_feature_names())
print('Got features')

lsa = TruncatedSVD(20)
dtm_lsa = lsa.fit_transform(dtm)
dtm_lsa = Normalizer(copy=False).fit_transform(dtm_lsa)

# print(pd.DataFrame(lsa.components_, index = list(range(100)), columns = vectorizer.get_feature_names()))
print('Did LSA')

similarity = np.asarray(np.asmatrix(dtm_lsa) * np.asmatrix(dtm_lsa).T)
#pd.DataFrame(similarity,index=names, columns=names)
outF = open('lsa.csv', 'w')
outF.write(((',' + ','.join(names)) + '\n' + '\n'.join(n + ',' + ','.join(str(i) for i in row) for n, row in zip(names, similarity))))
outF.close()
