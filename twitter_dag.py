from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl

default_args = {
    #'owner': 'airflow',
    #'depends_on_past': False,
    'start_date': datetime(2024,1,1),
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    #'retries': 1,
    #'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Our first DAG with ETL process !',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='twitter_etl_2',
    python_callable=run_twitter_etl,
    dag=dag,
)
run_file_transfer = BashOperator(
    bash_command='file_transfer.sh',
    task_id='twitter_etl_1',
    dag=dag
)


run_file_transfer >> run_etl