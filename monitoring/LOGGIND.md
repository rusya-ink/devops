# Monitoring and Metrics

## Stack

Logging example was taken from https://github.com/black-rosary/loki-nginx , from lab task.

In example were used:

- Loki
- Cadvisor
- Prometheus (for Metrics)
- Promtail

I added my web application to this stack.

## Report logging

Command for running is ```docker-compose up```.
After build go to http://localhost:5000 and use "admin" for login and password. 
![Grafana enter screen](screenshots/logging/enter.png)
In the expore tab you will see logs and metrics.
![Grafana LOKI logs, 1](screenshots/logging/LOKI1.png)
![Grafana LOKI logs, 2](screenshots/logging/LOKI2.png)
Here is how it looks from cinfiguration tab.
![Grafana config tab](screenshots/logging/config_tab.png)


## Best practices logging

- A dashboard should tell a story or answer a question. (It should be meaningful to use logs).
- Dashboards should reduce cognitive load, not add to it. (It should be easy to fing information from logs, find erros or warnings).
- For fast dashboard creation we should use templates.
From https://grafana.com/docs/grafana/latest/best-practices/best-practices-for-creating-dashboards/.

## Report metrics

Metrics could be seen in Grafana GUi and on Prometheus site.
![Metrics in Grafana GUi](screenshots/metrics/metrics_grafana_gui.png)
![Metrics in Prometheus GUi](screenshots/metrics/metrics_prometheus_gui.png)

## Best practices metrics

- Metrics should be atomic (have signle unit).
- Metric names should be understandable.
- Metric names should not be changed often (ideally they should not change at all through the projects0
From https://prometheus.io/docs/practices/naming/.