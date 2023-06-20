import csv
import boto3
import os
from datetime import datetime, timedelta

# Nome do arquivo CSV para exportar os dados
CSV_FILENAME = 'billing_data.csv'

# Obtendo as credenciais da variável de ambiente
access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Obtendo a região da variável de ambiente
region = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')

# Criação do cliente do serviço AWS Cost Explorer
cost_explorer = boto3.client('ce', aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             region_name=region)

# Obtendo o período completo do mês anterior
today = datetime.today()
last_day_of_previous_month = datetime(today.year, today.month, 1) - timedelta(days=1)
first_day_of_previous_month = datetime(last_day_of_previous_month.year, last_day_of_previous_month.month, 1)

start_date = first_day_of_previous_month.strftime('%Y-%m-%d')
end_date = last_day_of_previous_month.strftime('%Y-%m-%d')

# Obtendo os dados de billing agrupados por serviço
response = cost_explorer.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        },
    ]
)

# Escrevendo os dados no arquivo CSV
with open(CSV_FILENAME, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Service', 'Cost'])
    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        cost = group['Metrics']['UnblendedCost']['Amount']
        writer.writerow([service, cost])

print(f"Dados exportados com sucesso para o arquivo '{CSV_FILENAME}'.")
