from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

def is_positive(text):
    # Hugging Faceのトークンとモデル名を設定
    huggingface_token = '***'
    model_name = 'abhishek/autonlp-japanese-sentiment-59363'
    
    # 事前学習済みモデルとトークナイザをロード
    model = AutoModelForSequenceClassification.from_pretrained(model_name, use_auth_token=huggingface_token)
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=huggingface_token)

    # pipelineでモデルとトークナイザーを明示的に指定
    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, framework="pt")
    
    # テキストを分類して結果を得る
    result = classifier(text)[0]
    print('classifier')
    print(classifier(text))
    print('result')
    print(result)
    
    # ラベルが「ポジティブ」
    return result['label'] == 'positive'

# テスト用の例
text = "死ね"
print(is_positive(text))