import pandas as pd
from datetime import datetime
import s3fs

def run_twitter_etl():
    df1 = pd.read_csv('/home/ubuntu/processing/tweets.csv')
    df2 = df1[['author','content','date_time','number_of_likes','number_of_shares']]
    df2.to_csv('s3://twitter-etl-bucket-avnish/refined_tweets.csv',index=None)
    #df2.to_csv('/home/ubuntu/airflow/twitter_dags/refined_tweets.csv',index=None)

#run_twitter_etl()

