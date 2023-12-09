import pandas as pd
import torch
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np

from db_config.config import Session
from db_config.models import Transactions
from transformers import DistilBertTokenizer, DistilBertModel

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')


def data_for_clustering():
    session = Session()
    query = session.query(Transactions.Product_ID, Transactions.Description, Transactions.Customer_ID).all()

    data_df = pd.DataFrame(query, columns=['Product_ID', 'Description', 'Customer_ID'])

    return data_df


def get_embeddings(description):
    inputs = tokenizer(description, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


def tokenize():
    df = data_for_clustering()
    print(df)
    df['embeddings'] = df['Description'].apply(get_embeddings)
    embeddings = np.vstack(df['embeddings'])

    pca = PCA(n_components=50)
    reduced_embeddings = pca.fit_transform(embeddings)

    k = 5
    kmeans = KMeans(n_clusters=k)
    df['cluster'] = kmeans.fit_predict(reduced_embeddings)

    print(df["cluster"])

