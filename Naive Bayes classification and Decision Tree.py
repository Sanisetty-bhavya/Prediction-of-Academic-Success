class_counts = df['Target'].value_counts()
prior_probs = class_counts / len(df)
print(prior_probs)
likelihood_probs = {}
for feature in df.columns[:-1]:
    for class_label, class_df in df.groupby('Target'):
        feature_probs = class_df[feature].value_counts(normalize=True).to_dict()
        for feature_value, prob in feature_probs.items():
            likelihood_probs[(feature, feature_value, class_label)] = prob
for key, value in likelihood_probs.items():
    print(f"{key}: {value:.3f}")
pxgiven_Graduate = 1
pxgiven_Dropout = 1
pxgiven_Enrolled = 1
for feature in df.columns[:-1]:
    feature_value = df.loc[0, feature]
    key_Graduate = (feature, feature_value, 'Graduate')
    key_Dropout = (feature, feature_value, 'Dropout')
    key_Enrolled = (feature, feature_value, 'Enrolled')

    pxgiven_Graduate = likelihood_probs.get(key_Graduate, 1e-6)
    pxgiven_Dropout = likelihood_probs.get(key_Dropout, 1e-6)
    pxgiven_Enrolled = likelihood_probs.get(key_Enrolled, 1e-6)

print(f"P(X|Graduate) = {pxgiven_Graduate:.6f}")
print(f"P(X|Dropout) = {pxgiven_Dropout:.6f}")
print(f"P(X|Enrolled) = {pxgiven_Enrolled:.6f}")

pGraduategiven_x = pxgiven_Graduate * prior_probs['Graduate']
pDropoutgiven_x = pxgiven_Dropout * prior_probs['Dropout']
pEnrolledgiven_x = pxgiven_Enrolled * prior_probs['Enrolled']

print(f"P(Graduate|X) = {pGraduategiven_x:.3f}")
print(f"P(Dropout|X) = {pDropoutgiven_x:.3f}")
print(f"P(Enrolled|X) = {pEnrolledgiven_x:.3f}")
#Decision Tree Classifier Accuracy:
df_encoded = pd.get_dummies(df, columns=['Marital status' ,'Application mode','Application order','Course','Daytime/evening attendance','Previous qualification','Previous qualification (grade)','Nationality','Mothers qualification','Fathers qualification','Mothers occupation','Fathers occupation','Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date','Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)','Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)','Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)','Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)','Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP'], drop_first=True)
X = df_encoded.drop('Target', axis=1)
y = df_encoded['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=40)
tree_classifier = DecisionTreeClassifier()
tree_classifier.fit(X_train, y_train)
tree_accuracy = tree_classifier.score(X_test, y_test)
print(f"Decision Tree Classifier Accuracy: {tree_accuracy:.2f}")
#Printing tree
plt.figure(figsize=(10, 5))
plot_tree(tree_classifier, filled=True, feature_names=X.columns, max_depth=5) 
plt.show()
