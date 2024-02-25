from transformers import pipeline

def is_positive(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    return result['label'] == 'POSITIVE' and result['score'] > 0.75  # スコアの閾値は調整可能
