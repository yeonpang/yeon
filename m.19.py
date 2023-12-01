# 타이타닉

# 1-1
"""
import pandas as pd

tr = pd.read_csv("data/train.csv")

"""
tr = pd.read_csv("data/train.csv")

print(tr)
print("\n-----------------------------\n")
# print(tr.head())


# 1-2. null 찾기
"""
res = tr.isnull().sum()
print(res)

"""

# 1-3.

"""
# print("\n-----------------------------\n")
res = pd.corsstab(tr["Embarked"], tr["Survived"])
print(res)

res.colimns = res.columns.map({0:"Dead", 1:"Alive"})
print(res)

"""


# 1-4.
"""
# print("\n-----------------------------\n")
res = pd.crosstab(tr["Age"], tr["Survived"])
print(res)


res.columns = res.columns.map({0:"Dead", 1:"Alive"})
print(res)"""

# 1-5.

"""
# print("\n-----------------------------\n")
res = pd.crosstab(tr["Pclass"], tr["Survived"])
print(res)

"""

# 1-6. 
"""
# print("\n-----------------------------\n")
res = pd.crosstab(tr["Pclass"], tr["Survived"])
print(res)"""


# 1-7.
"""
# print("\n-----------------------------\n")

res = pd.crosstab(tr["Sex"], tr["Survived"])
print(res)
"""


# 1-8.

""" tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")
tr["Title"].value_counts()

# print(tr)

"""

# 1-9. 
"""
print(tr["Age"].isnull())
print(tr["Age"].isnull().sum())

"""

# 1-10.
"""
meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge) """

# 1-11.
"""

for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]
    
print(tr["Age"].head(20))

"""

# 1-12.
"""
tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
print(tr.head())"""

"""
tr["AgeCate"] = tr.AgeCate/astype(int)
print(tr.head())
print(tr.dtypes)

"""

# 1-13.
""" tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
print(tr["CabinCate"].value_counts()) """

# 1-14.

""" tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
# print(tr["CabinCate"].value_counts())

print(tr)"""


# 1-15.

""" res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res) """

# 1-16. 
"""
tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
# tr.FareCate = tr.FareCate.astype(int)
print(tr["FareCate"].value_counts()) """

# 1-17.

""" res = pd.corsstab(tr["FareCate"], tr["Survived"])
print(res)

"""

# 2-1.
"""
import pandas as pd

df = pd.read_csv("./data/Iris.csv", index_col="Id")
print(df.head())"""


# 2-2.
"""
df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
) """

"""
ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"}
)

print(df.head())

"""

# 2-3.

"""
df.iloc[:, [0, 1, 4]]
# res = ir.iloc[:, [0, 1, 4]]
print(res)"""

#2-4.
"""
df["품종"] = df["품종"].str[5:]
print(df)

"""

# 2-5.

"""
res = df.groupby("품종").mean()
print(res) """

""" res = df["품종"].value_counts()
print(res) """


# 3-1.

import matplotlib.pyplot as plt

"""
# value = [1, 2, 3, 4]
value = [5, 4, 5, 7, 10]
res = plt.plot(value)
plt.show()
"""

""" x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value)
plt.plot([2, 3, 6, 7, 10 ], [1, 4, 5, 8, 9])
plt.show()"""

"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}


plt.plot("x_data", "y_data", data=dic_val)
plt.show()

"""


#3-2.
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data")
plt.ylabel("y_data")
plt.show()
"""


""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad=15)
plt.ylabel("y_data", labelpad=50)
plt.show() """

"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad=10, loc="right")
plt.ylabel("y_data", labelpad=10, loc="top")
plt.show() """

"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}


plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad=10, loc="left")
plt.ylabel("y_data", labelpad=10, loc="bottom")
plt.show() """

# 3-3.
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
plt.show() """

# 3-4.
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend()
plt.show()"""

"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")


# plt.legend(loc=(1, 1))
# plt.legend(loc="best")

plt.legend(loc="lower right")
plt.show()"""


"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=1)
# plt.legend(ncol=2)
plt.show()"""

"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=2, fontsize=20)
plt.show()

"""

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.legend(ncol=2, fontsize=20, frameon=True)
plt.legend(ncol=2, fontsize=20, frameon=False)
plt.show() """

"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=2, fontsize=10, shadow=True)
# plt.legend(ncol=2, fontsize=10, shadow=False)
plt.show()
"""

# 3-5. 

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

plt.xlim()
plt.ylim()

plt.show() """


""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()

print(x_min, x_max)
print(y_min, y_max)"""


"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()

plt.xlim(x_min - 0.6, x_max)
plt.ylim(y_min - 0.6, y_max)

plt.show()
"""

"""dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()

# plt.xlim([0, 10])
# plt.ylim([0, 10])


plt.xlim([0, 50])
plt.ylim([0, 50])

plt.show()"""

"""
x_min, x_max, ymin, ymax = plt.axis()
print(x_min, x_max, ymin, ymax)"""

"""
plt.axis([0, 10, 0, 10]) """

"""
plt.axis("square")
# plt.axis("scaled")
# plt.axis("equa")
# plt.axis("tight")
# plt.axis("auto")
# plt.axis("on")
# plt.axis("off")"""

# 3-6.

""" plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], “ - - “, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], “ : “, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], “ . “, label="PData(km)") """

"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
"""





