# wip-limit

1) I will pass a dataset of development items from a team. I also want an analysis to identify patterns, but first I need you format the data to be analyzed. Format as data to best standard.

2) Based on the sent dataset, perform an EDA analysis generating the corresponding graphs. Also identify pattners, potential problemss and oppoortunities for improvment based on this data.

3) Based on the provided dataset, genrate a stacked column chart for lead time breakdown, showing the lead time for each phase individually proccess for eash work itemn. The phases to be considered are from "Prioratized" to "deployed", explicitly incluing the "development" phase. Do this only for items with status equal "deployed" the date in the "status_change_date" column and of all types using the column "issue_type_name". Sort by the "issue_type_name" column, in ascending order. Use a warm color palette to differentiate the phases of the graph. For each phase, caculcate the lead tiem considering the beginning of the current phase until the beginning of the next phase, and for the last phase ("deployed"), calculate the time until the completion date ("issue_type_name") when the last status is "deployed" Use plolty express if you need. can you generate the charts here ?

4) generate a CFD chart using plotly express and identify which phase is the bottleneck in this dataset, status_to_name" column, Please, put the order the status to: "to do", "in preparation", "prioritized", "In progress", "review", "accepted", "can't fix", "deployed"

5) generate another CFD chart in order to reduce the lead time in 3 days. you can use the bottleneck identified to do that action. In case you see any status that could be removed, do it.

6) based on the dataset provided, tell me Cycle time, Throughput

7) Analyzing the scenario that I have 15 items in my WIP, 2 developers and 2 QA members, how should be my WIP to have a cycle time equal 15 days? you can provide a chart representing this scenario.

8) calculate for me throughput rate day, arrival of items day

9) merge all code you created to generate all charts using just one execution. Also keep the prints with information. use plotly express for that purpose

10) onsidering the backlog with 40 items and a possibility of 3 of these items will be blocked for one week, which will be the projection date to finish using a Monte Carlo simulation. Use the throughout rate to calculate it. Produce the chart in plotly express if you want, create this chart date in axy X, add the percentile of completion of 50%, 75%, 85% and 90% in that same chart

11) Generate a bar char with the best WIP to achieve 40 items in backlog, consider 5 developers and 2 QA, use the throughput rate calculated and from now until the date of the 95% of certain confidence. don't forget that during this time, we can have 3 bugs that should be deal with an expedite items.

12) generate again adding this same number of WIP in axi Y and date in axi X. My intention is to have a simulation of WIP for each date until the date of completion

13) 




