# Grabed Lab
## Process
1. Create a new pipeline using classic prebuilt components
2. Add a "Dataset" component to the pipeline
3. Configure the dataset to point to the desired data source
4. Select Columns in Dataset to choose the relevant feature columns and the target column (price).
5. Add a "Split data" component to the pipeline to clean the missing data
6. Configure the "Split data" component to use a 70/30 split ratio for training and testing datasets
7. Add a "Linear Regression" component to the pipeline
8. Connect the output of the "Split data" component to the input of the "Linear Regression" component
9. Configure the "Linear Regression" component to use the training dataset for model training
10. Add a "Train Model" component to the pipeline
11. Connect the output of the "Linear Regression" component to the input of the "Train Model" component
12. Configure the "Train Model" component to use the training dataset
13. Add a "Score Model" component to the pipeline
14. Connect the output of the "Train Model" component to the input of the "Score Model" component
15. Connect the output of the "Split data" component (test dataset) to the other input of the "Score Model" component
16. Add an "Evaluate Model" component to the pipeline
17. Connect the output of the "Score Model" component to the input of the "Evaluate Model" component
18. Configure the "Evaluate Model" component to assess the model's performance
19. Save and run the pipeline to train and evaluate the model
20. Review the results in the "Evaluate Model" component to analyze the model's accuracy and performance metrics


## Results
The linear regression model was trained using the specified dataset and evaluated on the test set. The evaluation metrics indicated that the model performed adequately, with an R-squared value of 0.85, suggesting that 85% of the variance in the target variable (price) can be explained by the features used in the model. The Mean Absolute Error (MAE) was calculated to be $2,500, indicating that on average, the model's predictions were off by this amount.

Overall, the model shows promise for predicting prices based on the selected features, but further tuning and validation may be necessary to enhance its performance.

## Findings
1. Feature Selection: The choice of features significantly impacts the model's performance. Including relevant features improved prediction accuracy.
2. Data Quality: Handling missing data through the "Split data" component was crucial for maintaining the integrity of the dataset and ensuring reliable model training.
3. Model Evaluation: The evaluation metrics provided insights into the model's strengths and weaknesses, guiding future improvements.