Machine Learning : 
It's an application of Artifical Intelligence where models are trained using existing datasets to predict in future situations without being explicitly programmed for it.
    - Supervised Learning (classification & regression)
    - Unsupervised Learning (clustering & association)
    - Semi Supervised Learning
    - Reinforcement Learning

Supervised learning uses labeled data, while an unsupervised learning algorithm does not.

Types of machine learning models -
    - Classification : Predicts a discrete class
    - Regression : Predicts a continuous value
    - Clustering : Discovers grouping of data
    - Association : Prediction of next possible behaviour
    - Dimensionality reduction : Reduction in size of data



Linear Regression :
    It is a type of supervised learning
    Linear Regression shows a linear relationship between dependent & independent variables
    The idea is to find a best fit line by minimising the error (loss function)

        - Single variate :
            https://github.com/Happ2y/reunderstanding-ML/blob/main/Linear%20Regression%20(Single%20Variate).py

        - Multi variate :
            In real life, A decision is affected by multiple parameters.
            y = m1x1 + m2x2 + . . . . . + mnxn + c
            House Pricing Model : https://github.com/Happ2y/predicting-house-pricing
            Diabetes Prediction Model : https://github.com/Happ2y/diabetes-prediction



Gradient Descent :
An algorithm where we try to global minimum of a given function using it's derivative.
    - Batch gradient descent : All the dataset values are fed at once
    - Mini Batch gradient descent : Data Scientist decides what number of dataset values are to be fed at one go
    - Stochastic gradient descent : 1 dataset value is fed at once (episodic)
    
    
K Means :
    Within K nearest neighbours, class with maximum occurence will be the class of the observation
    Overfitting : When k value is too small, model fits too properly with training data
        Low training error
        Hight testing error
        In order to prevent overfitting, we can either resample the training datset or hold some dataset for validation.
    Underfitting : When k value is too large, irrevelent neighbours are being considered
    
    K = sqrt(n), n = size(dataset)
    Pros : Simpler approach
    Cons :
        Complexity in finding k value for highest accuracy
        Computational complexity in finding distance for classification

Logistic Regression :
It predicts a continuous value (probablity), which is then used to classify observations into classes. Therefore, It is a regression model that does classification.
