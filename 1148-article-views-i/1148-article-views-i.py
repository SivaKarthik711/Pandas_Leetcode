import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    viewed_self = views[views['author_id']==views['viewer_id']]
    viewed_self = viewed_self[['author_id']].drop_duplicates().sort_values(by='author_id', ascending=True)
    return viewed_self[['author_id']].rename(columns= {'author_id' : 'id'})
     
