# 📊 Dashboard de Análise Técnica de Laboratório (Portfólio)

Este projeto simula um dashboard de Business Intelligence completo para a gestão técnica de um laboratório, substituindo controlos manuais e focando na performance operacional, gestão de prazos e eficiência das equipas.

*(**Disclaimer:** Todos os dados apresentados são 100% fictícios, gerados com Python (Faker) e anonimizados. Nenhuma informação real da empresa está exposta.)*

---
## 1. O Desafio 🎯

O objetivo deste projeto foi centralizar os dados operacionais e criar uma ferramenta de gestão em tempo real. O desafio era dar visibilidade total ao funil de trabalho, que até então era controlado manualmente em planilhas.

As perguntas-chave a serem respondidas eram:
* Qual é o nosso backlog total (em quantidade e valor)?
* Onde estão os nossos principais gargalos de processo (Coleta vs. Pendente vs. Concluído)?
* Quais ensaios são mais rentáveis e quais são os mais demorados?
* Como está a performance de entrega em relação aos prazos prometidos?
* Qual a produtividade de cada célula de trabalho (bancada/laborista)?

## 2. A Solução: Dashboard Power BI 💡

Desenvolvi um dashboard no Power BI com 6 abas interligadas, cada uma com um objetivo claro:

* **📈 Gestão de Amostras:** Visão macro do funil, com KPIs de Quantidade para amostras "Em Coleta", "Pendente" e "Concluída".
* **💰 Gestão de Valores:** Visão financeira do funil, mostrando a distribuição do valor (R$) em cada etapa do processo e os ensaios mais rentáveis.
* **📋 Detalhes da Ficha:** Visão operacional por Ficha de Coleta, identificando o status de "gargalo" (o ensaio que está a travar a ficha) e a carga de trabalho.
* **🔬 Gestão de Ensaios:** Foco na performance, com rankings de ensaios, tempo médio de execução (TAT) e um filtro crucial de Interno vs. Externo.
* **🏭 Gestão Células:** Análise de produtividade, mostrando a distribuição de amostras, ensaios e valor por cada célula/bancada do laboratório.
* **⚠️ Gestão Pendências:** Uma aba de alerta focada apenas nas amostras que já passaram da data prometida, detalhando onde estão os atrasos.

## 3. Arquitetura e Destaques Técnicos 🛠️

Este projeto foi construído de ponta a ponta, simulando um ambiente empresarial completo:

* **SQL (Data Modeling):** O coração do projeto. Criei uma única `VIEW` no SQL Server que consolida 6 tabelas (Amostras, Ensaios, Clientes, Propostas, Células de Trabalho). Esta `VIEW` já contém toda a lógica de negócio, como a classificação de status (`categoria_status`), o cálculo de dias em atraso (`dias_em_atraso`) e a lógica de "gargalo" da ficha (`status_gargalo_ficha`). O script está na pasta `/SQL`.

* **DAX (Business Logic):** Desenvolvi medidas DAX avançadas para garantir a precisão dos KPIs, incluindo:
    * Uma lógica de "funil" (Coluna Calculada `Status Funil da Amostra`) para garantir que cada amostra seja contada em apenas uma categoria.
    * Medidas `SUMX` que calculam o valor por amostra (`valorconfirmado`), evitando a dupla contagem de valores.
    * Medidas de formatação dinâmica para os visuais e tooltips.

* **Anonimização de Dados (Python):** Para este portfólio, usei um script Python com as bibliotecas `Pandas` e `Faker` para gerar um arquivo Excel com +2.000 linhas de dados fictícios que replicam a estrutura exata da `VIEW` original. O script está na pasta `/Python-Anonimizacao`.

## 4. Demonstração em Ação 🎬

Screenshots/demo_dashboard.gif

## 5. Ficheiros do Projeto

* **`/` (Raiz):**
    * `Dashboard BI Técnico - PORTFÓLIO.pbix`: O dashboard final do Power BI.
    * `vw_bi_tecnico_operacional_fake.xlsx`: A fonte de dados falsos em Excel.
* **`/SQL`:** Contém o script T-SQL completo para criar a `vw_bi_tecnico_operacional`.
* **`/Python-Anonimizacao`:** Contém o script `gerar_dados_fake.py`.
* **`/Screenshots`:** Contém imagens das principais abas do dashboard.
