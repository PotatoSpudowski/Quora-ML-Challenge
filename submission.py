import sys
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
# from sklearn.svm import LinearSVC
from sklearn import preprocessing

"""
This is my submission for the Quora Answer Classifier challenge.
Submission score : 87
Submission rank : 69
"""


#Getting data
 
N, M = input().split()
N, M = int(N), int(M)

X = []
y = []
qid = []
X_pred = []
y_pred = []
for i in range(N):
    ll = input().split()
    y.append(int(ll[1]))
    ll = ll[2:]
    for j in range(len(ll)):
        ll[j] = float(ll[j][(ll[j].find(':')+1):])
    X.append(ll)

num = int(input())
for i in range(num):
    ll = input().split()
    qid.append(ll[0])
    ll = ll[1:]
    for j in range(len(ll)):
        ll[j] = float(ll[j][(ll[j].find(':')+1):])
    X_pred.append(ll)

#Scaling data

X = preprocessing.scale(X)
X_pred = preprocessing.scale(X_pred)

#Classifier

# clf = GradientBoostingClassifier( n_estimators=225, max_depth=3, learning_rate=0.3)
clf = RandomForestClassifier(n_estimators = 16, min_samples_leaf=9)
aboost = AdaBoostClassifier(base_estimator=clf, learning_rate=0.5, n_estimators=8)
# clf = LinearSVC()

aboost.fit(X, y) #Fitting classifier
y_pred = aboost.predict(X_pred) #Predicting using classifier

#Converting to output required by the challenge
for i in range(len(qid)):
    print(qid[i],end='')
    if(y_pred[i]==1):
        print(' +1')
    else:
        print(' -1')
