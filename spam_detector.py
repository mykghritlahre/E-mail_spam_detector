import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv("spam.csv")


encoder = LabelEncoder()
df['encoded_category'] = encoder.fit_transform(df['Category'])
df = df.drop(['Category'], axis='columns')


inputs = df["Message"]
outputs = df['encoded_category']

x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2)

vectorizer = CountVectorizer()
x_train_vectored = vectorizer.fit_transform(x_train)
x_test_vectored = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vectored, y_train)

score = model.score(x_test_vectored, y_test)
print(f"Model Accuracy: {score}")


def predict_spam(email):
    email_count = vectorizer.transform([email])
    prediction = model.predict(email_count)
    return "spam" if prediction[0] == 1 else "ham"


emails = [
    'Hey mohan, can we get together to watch football game tomorrow?',
    'Upto 20 % discount on parking, exclusive offer just for you. Dont miss this reward!'
]

for email in emails:
    print(f'({email}) is a {predict_spam(email)}')