***INTRODUCTION:***

This Python script serves as a sophisticated tool for predicting student outcomes, emphasizing dropout prediction and academic success. Through a combination of data mining, association rule extraction, and machine learning, the script offers a holistic and insightful approach to addressing challenges in the realm of education. The comprehensive analysis and predictive modeling aim to assist educational institutions in identifying students at risk of dropout and promoting academic success.

1. **Data Preprocessing:**
   - **Pandas and Label Encoding:** The script utilizes the Pandas library to read and manipulate the dataset ('projectdata.csv'). Categorical variables are encoded into numerical format, establishing the groundwork for subsequent analyses.

2. **Association Rule Mining (FP-Growth Algorithm):**
   - **Frequent Itemsets and Association Rules:** The FP-Growth algorithm is employed to mine frequent itemsets from the dataset, revealing intricate patterns and correlations among various attributes. The script showcases frequent itemsets and associated rules, providing valuable insights into factors influencing student outcomes.

3. **Decision Tree Classification:**
   - **Information Gain, Gain Ratio, and Gini Index Models:** Three Decision Tree classifiers are trained using different criteria—Information Gain, Gain Ratio, and Gini Index. Visualizations of the resulting tree structures offer an intuitive understanding of the learned patterns.

4. **Naive Bayes Classification:**
   - The script employs a Naive Bayes classification approach to calculate probabilities. Although the specific implementation details for Naive Bayes are not explicitly provided in the script, the probability calculations are conducted to estimate the likelihood of belonging to different classes given certain feature values.
   - Probabilities such as P(X|Graduate), P(X|Dropout), and P(X|Enrolled) are computed using Naive Bayes assumptions.
- Decision Tree Classification:
  - The script utilizes Decision Tree models to predict student outcomes.
  - Likelihood probabilities for specific feature values are calculated using the Decision Tree models, contributing to the overall probability-based analysis.
  - Probability estimates aid in understanding the predictive power of the Decision Tree models regarding the likelihood of students falling into different classes (Graduate, Dropout, Enrolled).
5. **Model Evaluation:**
   - **Accuracy and Classification Reports:** The script concludes with a robust evaluation of the Decision Tree models. Accuracy scores and detailed classification reports for a test set provide a comprehensive assessment of the models' predictive capabilities.

![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/515ee274-c7b4-47b1-8f68-36bff9c1dddf)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/d4c115d8-0cbe-491f-8564-4cb017280cc4)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/0e61cbc0-7840-4f2e-8455-87a1e563928d)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/02c3d6ba-5f84-4249-bc2d-a68b5bb6bdfe)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/61d761ad-e738-49f7-89be-3f2e887ed5c7)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/befd9dc3-c3f2-4000-9f65-e724dd3f0f23)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/e7e04565-3e48-46a6-8748-81c41ded881f)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/367d222c-caf2-42db-8067-b19696c1d967)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/e54a814a-b4b7-4f54-9d0f-8dde1d3c28ab)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/83f15bcb-fd33-4e37-bb82-5932c026e79e)

![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/14057112-2cde-4214-b885-9d5a14cd3616)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/d69c64ab-c014-4ef7-b9a1-b1afd2663e49)
![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/3f22d253-4b88-46f2-bcb9-f7d9a7f151ce)

![image](https://github.com/Sanisetty-bhavya/Prediction-of-Academic-Success/assets/114378144/d820a68f-67aa-419b-9be7-7495a8bf4ac4)
