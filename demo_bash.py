from airflow import dag
from airflow.operators import BashOperator
from datetime import datetime


default_arg=(
        'start_date'=datetime.now()
        'retries':1
)


dag=dag(
    'bash_airflow'
    default_arg=default_arg
    schedule='*/10****'
)

print_test = BashOperator(
    target_id='id'
    bash_command='echo test'
    dag=dag
)

