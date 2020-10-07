from config import save_cfg, load_cfg, reset_cfg
from news import get_news, display
from flask import Flask

app = Flask(__name__)

@app.route('/')
def handler():
  cfg_data = load_cfg()
  articles = get_news()
  filtered_articles = []
  for i in articles:
    id = i['id']
    if id not in cfg_data['seen']:
      cfg_data['seen'][id] = True
      filtered_articles += [i]
  save_cfg(data=cfg_data)
  return display(filtered_articles)
