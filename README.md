# Exoplanet-Classification

### **Team Members**
* Vinod Singh Rathore - 2301ME54
* Swapnil Kumar Baranwal - 2301MM17
* Aditi Kashyap - 2301EC03
* Rishav Anand - 2301MM34

### **Objective**
To build a logistic regression classifier to identify exoplanets using the Kepler labelled time series data, based on flux measurements across time steps.

### **Introduction**
Logistic Regression is a widely used machine learning algorithm for binary classification problems. In this project, it helps us determine whether a given star, based on its flux time series data, is likely to have an exoplanet or not.

* How It Works:
Logistic regression estimates the probability that a given input (i.e., a star’s flux pattern) belongs to a particular class.

    * It applies a sigmoid function to transform the linear combination of input features into a value between 0 and 1.

    * This probability is then thresholded (commonly at 0.5) to assign a binary class label.

* Why Use Logistic Regression for This Task?
It’s simple and interpretable, making it a good starting point for classification tasks.

    * It performs well on high-dimensional datasets like ours (with 3,197 features).

    * It serves as a baseline model to compare with more complex methods later (e.g., Random Forest, SVM, Neural Networks).

### **Dataset Description**

Downloaded from [Kepler Labelled Time Series Dataset on Kaggle](https://www.kaggle.com/datasets/keplersmachines/kepler-labelled-time-series-data) 

The dataset used in this project is the Kepler Labelled Time Series Dataset, which contains flux measurements collected from stars observed by the Kepler space telescope. Each star's light intensity is recorded at 3,197 different time steps, representing how the brightness of the star changes over time.

Number of Features:
Each sample contains `3,197 flux values (FLUX.1 to FLUX.3197)` representing the star's brightness at different time intervals.

Training Set:
The training dataset (exoTrain.csv) contains `5087
samples`.

Testing Set:
The testing dataset (exoTest.csv) contains `570 samples`.

Label Description:
The LABEL column indicates whether a star is an exoplanet candidate:

LABEL -> `2 is an exoplanet star` and `1 is a non-exoplanet-star`.


### **Discussion & Insights**
The logistic regression model achieved a respectable accuracy on the test dataset, demonstrating its ability to capture patterns in the flux time series data. However, several points are worth discussing in terms of model performance, limitations, and future improvements.

* Is Logistic Regression Enough?
While logistic regression is a solid starting point for binary classification, it may not be sufficient for capturing the complex, non-linear relationships that likely exist in astronomical time series data. The fact that the input consists of thousands of sequential flux values suggests that more advanced models could better interpret underlying trends, dips, and periodic patterns associated with exoplanet transits.

* Limitations of Logistic Regression
    * Linear Decision Boundary: Logistic regression assumes a linear relationship between input features and the log-odds of the output. This can limit performance in datasets where the decision boundary is non-linear, as is often the case with time-series data.

    * High Dimensionality: With 3,197 features per sample, logistic regression may struggle without dimensionality reduction. While normalization helps, the presence of irrelevant or noisy flux values could impact accuracy.

    * No Temporal Understanding: Logistic regression does not consider the sequence or temporal order of flux values, which is critical in identifying transiting exoplanets.

* Potential Improvements

    To improve model performance and better exploit the structure of the dataset, several enhancements can be considered:

    * Dimensionality Reduction: Techniques like Principal Component Analysis (PCA) can be used to reduce the feature space while preserving important variance, which can improve both performance and training speed.

    * Advanced Classifiers: Trying non-linear models such as:

        * Random Forests or Gradient Boosting for better interpretability and robustness.

        * Support Vector Machines (SVMs) with appropriate kernels for non-linear decision boundaries.

        * 1D Convolutional Neural Networks (CNNs), which are particularly suited for time-series data as they can detect patterns over sequential windows.

    * Class Balancing: If the dataset is imbalanced (e.g., fewer exoplanet stars than non-exoplanet stars), applying techniques like SMOTE or using class weights can help improve recall on the minority class.

### **Conclusion**
In this project, we used logistic regression to classify stars as exoplanet-hosting or not, based on flux data from the Kepler dataset. Without applying any advanced preprocessing or feature engineering, the model achieved a high accuracy of 98.95% on the test set.

This demonstrates that logistic regression can perform well even on raw time series data when properly structured.

