# Mission Control - Space Connect

## Integrantes

- Davi Simoncelo — RM: 571738 — Turma: 1CCPK
- João Pedro Sousa — RM: 573962 — Turma: 1CCPK
- Matheus Evangelista Silva — RM: 568593 — Turma: 1CCPK

## O que é o projeto:

O Mission Control App é um sistema de simulação e monitoramento em terminal desenvolvido em Python. Ele foi desenvolvido sobre o contexto de missões espaciais de longa duração, sendo elas divididas em 6 ciclos. e sendo analisadas por ciclo as áreas de "Temperatura interna", "Comunicação com a base", "Sistema de energia","Suporte de oxigênio","Estabilidade operacional".

## Funcionalidades:

A aplicação é capaz de gerar dados simulados de forma aleatória ou manual, gerar relatórios para cada ciclo, por área ou de forma geral e criar um histórico por sessão, permitindo visualizar, retomar os dados antigos de análise para os atuais ou apagar um histórico.

## Como executar:

```bash
git clone https://github.com/MatheusSilva-Inf/Space-Connect-Global-Solution-2026
cd Space-Connect-Global-Solution-2026
python -m venv .venv
.venv\Scripts\activate
python mission_control.py
```

## Limitações:

- Sem persistência de histórico entre sessões
- Interface apenas via terminal
- Foi testado com interpretador 3.10+ apenas

# Vídeo de demonstração:

