# API MVP Modelo Heart Disease

Esta é a API do modelo de machine learning que auxilia no diagnóstico de doenças cardíacas.

## Como utilizar:

1. Clone este repositório:
git clone https://github.com/MatheusVinicius77/api-mvp-heart-disease/tree/master

2. Navegue até o diretório `api-mvp-heart-disease/`:
cd api-mvp-heart-disease/

3. Construa a imagem Docker:
docker build -t <nome_imagem> .

4. Execute o contêiner Docker:
docker run -d -p <porta>:3002 <nome_imagem>:latest


Substitua `<nome_imagem>` pelo nome desejado para a imagem. Sugestão: `mvp_api`.

Substitua `<porta>` pela porta desejada que será equivalente à porta da API (3002). Sugestão: `3002`.

