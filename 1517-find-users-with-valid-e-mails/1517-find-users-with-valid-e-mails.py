import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
     email_pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
     users = users[users['mail'].str.match(email_pattern,na =False)]
     return users