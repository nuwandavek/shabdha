import json
import pandas as pd
from pathlib import Path
from torch.utils.data import TensorDataset, DataLoader


class Tokenizer:
  def __init__(self):
    language_unicode_mapping = {
      'en': list(range(97, 123)),
      'kn': list(range(3202, 3277)),
    }
    self.vocab_dict = {}
    start_idx = 10
    for lang, unicode_list in language_unicode_mapping.items():
      for unicode in unicode_list:
        self.vocab_dict[chr(unicode)] = start_idx
        start_idx += 1
    self.vocab['|START|'] = 0
    self.vocab['|END|'] = 1
    self.vocab['|UNK|'] = 2
    self.inv_vocab = {v: k for k, v in self.vocab.items()}

  def encode(self, text):
    return [self.vocab_dict.get(x, 2) for x in text]

  def decode(self, tokens):
    return "".join([self.inv_vocab[x] for x in tokens])


class Dataset:
  def _init__(self, data_path):
    self.data_path = data_path
    self.tokenizer = Tokenizer()
    self.df_dict = self.load_data(data_path)

  def load_data(self, data_path):
    df_dict = {}
    for file in Path(data_path).glob("*.json"):
      with open(file) as fob:
        data = [json.loads(x) for x in fob.read().strip().split("\n")]
        df = pd.DataFrame(data)
      if "train" in file.name:
        df_dict["train"] = df
      elif "test" in file.name:
        df_dict["test"] = df
      elif "val" in file.name:
        df_dict['val'] = df
    return df_dict

  def create_dataset(self):
    
  
  def get_dataset(self, split):
    df = self.df_dict[split]

    return 


  def explode_rows(self, row):
    native_word_tokens = self.tokenizer.encode(row['native_word']) + [self.tokenizer.vocab['|START|']]
    english_word_tokens = self.tokenizer.encode(row['english_word']) + [self.tokenizer.vocab['|END|']]
    rows = []
    for i in range(len(english_word_tokens)):
      rows.append(native_word_tokens + english_word_tokens[:i])
    



