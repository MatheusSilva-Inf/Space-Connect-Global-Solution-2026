# Mission Control - Space Connect

## Integrantes

- Davi Simoncelo — RM: 571738 — Turma: 1CCPK
- João Pedro Sousa — RM: 573962 — Turma: 1CCPK
- Matheus Evangelista Silva — RM: 568593 — Turma: 1CCPK

## O que é o projeto:

O Mission Control App é uma solução imaginada para facilitar a intuitividade e agilidade em tomadas de decisões durante missões espaciais de longa duração. Para o contexto do aplicativo é imaginado que essas missões possuem 6 ciclos e em cada um deles é analisado as áreas de "Temperatura interna", "Comunicação com a base", "Sistema de energia","Suporte de oxigênio","Estabilidade operacional" da nave, emitindo alertas e recomendações com base na gravidade do problema.

## Funcionalidades:

- Geração dados simulados de forma aleatória ou manual, 
- Geração de relatórios para cada ciclo, por área ou de forma geral
- Geração de recomendações da missão ou para cada área analisada
- Criação um histórico por sessão, permitindo visualizar, retomar os dados antigos de análise para os atuais ou apagar um histórico.

## Como executar:

```bash
git clone https://github.com/MatheusSilva-Inf/Space-Connect-Global-Solution-2026
cd Space-Connect-Global-Solution-2026
python -m venv .venv
.venv\Scripts\activate
# Linux abaixo
# source .venv/bin/activate
python mission_control.py
```

## Limitações:

- Sem persistência de histórico entre sessões
- Interface apenas via terminal
- Foi testado com interpretador 3.10+ apenas

# Vídeo de demonstração: https://youtu.be/_XN1DLWqsfQ

