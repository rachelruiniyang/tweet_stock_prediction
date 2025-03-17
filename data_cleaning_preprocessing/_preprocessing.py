import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import emoji

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize objects
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def filter_by_date(df1, df2):
    start_day = min(df1['day_date'])
    end_day = max(df1['day_date'])
    
    print(f"Start day: {start_day}")
    print(f"End day: {end_day}")
    
    # Filter based on the date range
    filtered_df = df2[(df2['day_date'] >= start_day) & (df2['day_date'] <= end_day)]
    
    return filtered_df

def preprocess_tweet(text):
    """
    Preprocesses a tweet by performing various cleaning and text normalization tasks.

    """
    text = text.lower()

    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    text = re.sub(r'@\w+', '', text)

    text = re.sub(r'#\w+', '', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))
    
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    text = ''.join([char for char in text if not emoji.is_emoji(char)])
    
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text
