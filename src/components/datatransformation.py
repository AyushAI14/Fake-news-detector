from text_prettifier import TextPrettifier
import pandas as pd
from src.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config=DataTransformationConfig):
        self.config=config
        
    def text_cleaner(self,text):
        prettifier = TextPrettifier()
        text = text.lower()
        text = prettifier.remove_contractions(text)
        text = prettifier.remove_emojis(text)
        text = prettifier.remove_html_tags(text)
        text = prettifier.remove_urls(text)
        # keep stopwords and punctuation for BERT or LSTM
        return text
    def tranform_text(self):
        df=pd.read_csv(self.config.df_output_path)
        df['text']=df['text'].apply(self.text_cleaner)
        df.to_csv(self.config.tranformed_data,index=False)

