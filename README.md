# Fake News Detection for Vietnamese Text

## Overview

This project addresses the critical issue of fake news in the era of information overload. It focuses on working with Vietnamese text data to build a fake news prediction model and deploy it on a simple web application.

## Features

- Process and analyze Vietnamese text data
- Build a machine learning model to predict fake news
- Deploy the model on a web application for easy demonstration

## Data Source

We use the [VNFD Dataset](https://github.com/thanhhocse96/vfnd-vietnamese-fake-news-datasets/blob/master/CSV/vn_news_223_tdlfr.csv), which contains:
- 223 Vietnamese news records
- Binary labels: 1 (fake news) and 0 (real news)

For detailed dataset information, see the [VNFD Dataset Description](https://github.com/thanhhocse96/vfnd-vietnamese-fake-news-datasets/tree/master/CSV).

## Text Preprocessing

Our preprocessing pipeline includes:
1. Lowercase conversion
2. Stopword removal
3. Stemming
4. Domain-specific normalization
5. Noise removal (HTML tags, special characters, punctuation)

Resources:
- [Text Preprocessing Overview](https://maelfabien.github.io/machinelearning/NLP_1/#i-what-is-preprocessing)
- [Vietnamese Stopwords](https://github.com/stopwords/vietnamese-stopwords/blob/master/vietnamese-stopwords.txt)
- [VnCoreNLP Tokenizer](https://github.com/vncorenlp/VnCoreNLP#install)

## Model Deployment

We use [Streamlit](https://streamlit.io/gallery) to create a simple web interface for our model, allowing for free deployment and easy demonstration.

[Live Demo](https://share.streamlit.io/beiryu/fake_new/main/fake_new_detection.py)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

[Add instructions on how to run the project locally]

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]

## Acknowledgements

- [VNFD Dataset creators](https://github.com/thanhhocse96/vfnd-vietnamese-fake-news-datasets)
- [Streamlit](https://streamlit.io/) for the web application framework
