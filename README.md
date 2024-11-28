# Spam Classifier with Streamlit

This project is a simple spam classifier web application built using Streamlit. The model uses natural language processing (NLP) techniques to classify emails as either **spam** or **ham** (non-spam). It leverages a dataset of spam emails and employs the **Naive Bayes** algorithm to perform classification. 

## Features
- **Email Classification**: Classify email messages as spam or ham based on their content.
- **Streamlit Interface**: A user-friendly web interface built with Streamlit where users can input an email and get predictions on whether it's spam or ham.

## Installation Instructions

### Prerequisites:
Make sure you have Python 3.x installed.

### Install the required libraries:

You can install the required libraries using `pip`:

```bash
pip install pandas scikit-learn streamlit
```

### Running the App:

1. **Clone this repository** or download the code files to your local machine.
2. Navigate to the folder where your files are located.
3. Run the following command in your terminal:

```bash
streamlit run app.py
```

This will open the Streamlit app in your default web browser.

## Files

- **spam.csv**: Contains a dataset of messages with their respective categories (spam or ham).
- **app.py**: The main Python file which contains the code for training the model and running the Streamlit interface.
- **requirements.txt**: A file listing all the required Python libraries.

## Model Description

1. **Data Preprocessing**:
   - The dataset (`spam.csv`) is read into a pandas DataFrame.
   - The target variable `Category` is encoded into numerical values using `LabelEncoder`.
   - Unwanted columns are dropped, and only the `Message` column is used for the input features.

2. **Feature Extraction**:
   - The `CountVectorizer` is used to convert text messages into numerical form using the bag-of-words model.

3. **Model Training**:
   - The **Multinomial Naive Bayes** classifier is used for training the model on the features.
   - The dataset is split into training and testing sets using `train_test_split` for model validation.

4. **Prediction**:
   - The trained model predicts whether a new email is spam or ham. The user can enter a message into the Streamlit interface and get a prediction.

## How to Use

1. Once the app is running, the interface will prompt you to input a message.
2. Enter any message or email content and hit **Classify**.
3. The system will display whether the message is classified as **spam** or **ham**.

### Example

- **Message**: "Hey mohan, can we get together to watch football game tomorrow?"
- **Prediction**: ham

- **Message**: "Upto 20 % discount on parking, exclusive offer just for you. Don't miss this reward!"
- **Prediction**: spam

## Model Evaluation

The accuracy of the model is evaluated on the test data, and the model's performance score is printed out. The higher the score, the better the model is at classifying spam messages.

