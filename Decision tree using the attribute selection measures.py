#a) information gain

df_encoded = pd.get_dummies(df, columns=['Marital status' ,'Application mode','Application order','Course','Daytime/evening attendance','Previous qualification','Previous qualification (grade)','Nationality','Mothers qualification','Fathers qualification','Mothers occupation','Fathers occupation','Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date','Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)','Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)','Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)','Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)','Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP'], drop_first=True)
X = df_encoded.drop('Target', axis=1)
y = df_encoded['Target']
clf_info_gain = DecisionTreeClassifier(criterion="entropy")
clf_info_gain.fit(X, y)
fig, ax = plt.subplots(figsize=(15, 5))
tree.plot_tree(clf_info_gain, feature_names=X.columns, class_names=clf_info_gain.classes_,filled=True,max_depth=5)
plt.title('Decision Tree with Information Gain')
plt.show()

# b) gain ratio

clf_gain_ratio = DecisionTreeClassifier(criterion="entropy", splitter="best")
clf_gain_ratio.fit(X, y)
fig, ax = plt.subplots(figsize=(15, 5))
tree.plot_tree(clf_gain_ratio, feature_names=X.columns, class_names=clf_gain_ratio.classes_,filled=True,max_depth=5)
plt.title('Decision Tree with Gain Ratio')
plt.show()

# c) gini index

clf_gini = DecisionTreeClassifier(criterion="gini")
clf_gini.fit(X, y)
fig, ax = plt.subplots(figsize=(15, 5))
tree.plot_tree(clf_info_gain, feature_names=X.columns, class_names=clf_info_gain.classes_, filled=True,max_depth=5)
plt.title('Decision Tree with Information Gain')
plt.show()
