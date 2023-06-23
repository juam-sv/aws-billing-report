# aws-billing-report

## Objetivo
O objetivo é a criação de função lambda que capture dados de cobrança da AWS, exporte-os para um arquivo CSV e gere um relatório visual com gráficos usando as bibliotecas Python. E também que extraia informações de valor, como tendências e otimização de custos, e enviar o relatório por e-mail. As possíveis tarefas para essa história de usuário são:

- Configurar a função lambda na AWS
- Implementar a lógica de captura de dados de cobrança da AWS
- Exportar os dados para um arquivo CSV
- Implementar a geração de relatórios visuais com gráficos usando as bibliotecas Python
- Investigar se há informações de valor a serem extraídas dos dados de cobrança
- Implementar a extração de informações de valor, se possível
- Configurar o envio de relatório por e-mail.

#### ToDo
- [ ] Adicionar um pipe de lint
- [ ] Complementar o README
- [ ] adicionar um costs.csv com exemplos de valores
- [ ] Iniciar um (jupyter) notebook para plotar os gráficos
- [ ] Criar um Dockerfile
# Running docker environment

Usage: make [`target`]

## Local Development

- `make up`: Start all or specified containers in the foreground.
- `make build`: Build all or specified containers.
- `make down`: Stop and remove all or specified containers.

## Other

- `make help`: Show this help.
