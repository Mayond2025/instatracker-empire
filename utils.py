
import pandas as pd

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def filter_by_keyword(posts, keyword):
    return [post for post in posts if keyword.lower() in post['description'].lower()]
