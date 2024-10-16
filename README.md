# API de Previsão com Regressão Linear

## URL da API na Azure
"https://sprint4-fiap-1tiaa-fjcmfffgbcdsa3cj.brazilsouth-01.azurewebsites.net"

Esta é uma API simples de previsão, construída usando Flask e implantada no Azure App Service. A API utiliza um algoritmo de regressão linear para realizar previsões com base em dois valores de entrada.

## Descrição do Projeto

Este projeto consiste em um serviço web que expõe um endpoint `/api/predict` para realizar previsões. O algoritmo é uma simples regressão linear, onde a fórmula é:

y = a * x1 + b * x2

Temos também o endpoint padrão `/`, que nos retorna um "API funcionando!"

## Como Utilizar o Predict

Faça uma requisição `POST` para o endpoint `/api/predict` com um corpo JSON como este:

```json
{
    "x1": 10,
    "x2": 20
}