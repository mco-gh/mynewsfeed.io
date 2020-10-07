from newscatcher import Newscatcher, describe_url
from config import cfg_data

# Function to get articles from a given site with a given topic...
def get_new_articles(site, topic):
  nc = Newscatcher(website=site, topic=topic)
  articles = nc.get_news()
  # Return the articles
  if articles:
    if 'articles' in articles:
      return articles['articles']
  return None

def get_news(sites=None, topics=None):
  if not sites:
    sites = cfg_data['sites']
  if not topics:
    topics = cfg_data['topics']
  all_articles = []
  for i in sites:
    topic_list = describe_url(i)['topics']
    for j in topics:
      if j not in topic_list:
        continue
      articles = get_new_articles(i, j)
      all_articles += articles
  return all_articles

# Define a function to generate an HTML or text version of our report.
def display(articles, fmt='html'):
  if len(articles) == 0:
    return "Nothing new to show you."
  report = '<table>' if fmt == 'html' else ''
  cnt = 1
  for i in articles:
    id = i['id']
    title = i['title']
    if fmt == 'html':
      report += f'<tr><td>{cnt}.</td><td><a target="_blank" href={id}>{title}</a></td></tr>\n'
    elif fmt == 'text':
      report += f'{cnt:2d}. {title:70.70s}  {id}\n'
    cnt += 1
  report += '</table>' if fmt == 'html' else ''
  return report
