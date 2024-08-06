# wip-limit

Prompt #1
Vou passar um conjunto de dados de itens de desenvolvimento de uma equipe. Também quero uma análise para identificar padrões, mas primeiro preciso que você formate os dados para serem analisados. Formate os dados no melhor padrão possível. Com base no conjunto de dados enviado, realize uma análise exploratória de dados (EDA) gerando os gráficos correspondentes. Também identifique padrões, potenciais problemas e oportunidades de melhoria com base nesses dados.

Prompt #2
Com base no conjunto de dados fornecido, gere um gráfico de colunas empilhadas para a decomposição do tempo de ciclo, mostrando o tempo de ciclo para cada fase individualmente para cada item de trabalho. As fases a serem consideradas são de "Priorizado" a "Implantado", incluindo explicitamente a fase de "Desenvolvimento". Faça isso apenas para itens com status igual a "Implantado" na data na coluna "status_change_date" e de todos os tipos usando a coluna "issue_type_name". Ordene pela coluna "issue_type_name" em ordem crescente. Use uma paleta de cores quentes para diferenciar as fases do gráfico. Para cada fase, calcule o tempo de ciclo considerando o início da fase atual até o início da próxima fase, e para a última fase ("Implantado"), calcule o tempo até a data de conclusão ("issue_type_name") quando o último status for "Implantado". Use plotly express se precisar. Você pode gerar os gráficos aqui?

Prompt #3
Gere um gráfico de barras com o melhor WIP para alcançar 40 itens no backlog, considere 5 desenvolvedores e 2 QA, use a taxa de produção calculada e de agora até a data de 95% de confiança. Não se esqueça de que durante esse tempo, podemos ter 3 bugs que devem ser tratados como itens urgentes. Adicionando esse mesmo número de WIP no eixo Y e a data no eixo X. Minha intenção é ter uma simulação de WIP para cada data até a data de conclusão.
