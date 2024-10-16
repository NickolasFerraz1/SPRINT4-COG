# API de Previsão com Regressão Linear

Esta é uma API simples de previsão, construída usando Flask e implantada no Azure App Service. A API utiliza um algoritmo de regressão linear para realizar previsões com base em dois valores de entrada.

## Descrição do Projeto

Este projeto consiste em um serviço web que expõe um endpoint `/api/predict` para realizar previsões. O algoritmo é uma simples regressão linear, onde a fórmula é:

y = a * x1 + b * x2

Temos também o endpoint padrão, que nos retorna um "API funcionando!"