# Backend

## Estrutura do projeto

- **api/:** diretório com o código fonte da API
- **artefatos/:** diretório com o código fonte dos artefatos
- **migrations/:** diretório com os arquivos SQL usados para a crição do banco de dados, nomeados conforme a ordem de execução que deve ser seguida

## Comandos Úteis

### Enviar mensagem para o RabbitMQ usando Docker e CLI:

```bash
# Entrando no container do rabbitmq
docker-compose exec rabbitmq sh

# Enviando mensagem com o usuário, senha e vhost padrão
rabbitmqadmin -u pi_dsm_5 -p pi_dsm_5 -V mensageria_pi_dsm_5 publish exchange=eventos_exchange routing_key=eventos payload="{\"artefato\": 1, \"corpo\": {\"mensagem\": \"sla\"}"
```