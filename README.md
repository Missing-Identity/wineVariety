# Wine Variety Prediction Model

## Overview

This document provides a brief overview of the wine variety prediction model developed using a dataset of wine reviews. The model was trained using features such as country, province, and review description, and predicts the variety of the wine.

## Model Development

The model was developed using a RandomForestClassifier, a powerful ensemble learning method that operates by constructing multiple decision trees during training and outputting the class that is the mode of the classes of the individual trees.

The data was preprocessed by encoding categorical features (country and province) using a LabelEncoder, and text data (review description) was vectorized using a TfidfVectorizer. The model was trained on this preprocessed data.

## Insights

The top five features that were found to be most important in predicting wine variety were:

1. Province: Bordeaux
2. Blend
3. Country: Portugal
4. Province: Piedmont
5. Tannins

These insights suggest that the province where the wine is produced and the blend of the wine are significant factors in determining its variety. Additionally, specific terms in the review description, such as "tannins", also play a crucial role.

## API Deployment

The model was deployed as a Flask API, which accepts POST requests with JSON data containing the country, province, and review description. The API preprocesses the input data in the same way as the training data, makes a prediction using the trained model, and returns the predicted wine variety.

Here is a sample POST request to the API:

```json
{
    "country": "France",
    "province": "Bordeaux",
    "review_description": "A blend of Merlot and Cabernet Sauvignon, this wine has strong flavors of blackberry and cherry, with a hint of oak."
}
```

## Error Handling

The model was designed to handle unseen labels in the country and province features by treating them as 'unknown'. It also handles missing values by filling them with 0.

## Assumptions
In the process of developing the wine variety prediction model, several assumptions were made:

Data Completeness: It was assumed that the data provided was complete and representative of the population of wines. If the dataset was biased or lacked certain varieties, countries, or provinces, the model's predictions could be skewed.

Label Accuracy: The model assumes that the labels provided in the dataset (i.e., the wine varieties) were accurate. If there were errors in the labeling, this could affect the model's ability to make correct predictions.

Feature Relevance: It was assumed that the features selected for the model (country, province, and review description) were relevant and had a significant impact on the wine variety. If there were other unconsidered factors that significantly affect the wine variety, the model might not perform optimally.

Textual Reviews: The model assumes that the textual reviews accurately describe the characteristics of the wine. It also assumes that the language used in the reviews is consistent and that similar terms are used to describe similar characteristics across different reviews.

Handling of Unseen Labels and Missing Values: For unseen labels in the country and province features, the model treats them as 'unknown'. This assumes that the impact of unseen labels on the prediction is negligible. Similarly, the model handles missing values by filling them with 0, assuming that these missing values do not significantly affect the prediction.

Model Assumptions: The RandomForestClassifier model assumes that a collection of (potentially) weakly predictive features can be combined to create a strong predictive model. It also assumes that the decision trees within the model are better than random guessing and uncorrelated with each other.



## Conclusion

This wine variety prediction model provides a robust method for predicting the variety of a wine based on its country, province, and a description of its taste. The insights derived from the model can be valuable for wine connoisseurs, distributors, and producers alike.
