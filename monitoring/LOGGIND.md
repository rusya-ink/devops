# Monitoring

## Stack

Logging example was taken from https://github.com/black-rosary/loki-nginx , from lab task.

In example were used:

- Loki
- Cadvisor
- Prometheus (for Metrics)
- Promtail

I added my web application to this stack.

## Report

Command for running is ```docker-compose up```.
After build go to http://localhost:5000 and use "admin" for login and password. 
![Grafana enter screen](screenshots/logging/enter.jpg)
In the expore tab you will see logs and metrics.
![Grafana LOKI logs](screenshots/logging/LOKI.jpg)
Here is how it looks from cinfiguration tab.
![Grafana config tab](screenshots/logging/config_tab.jpg)


## Best practices

- A dashboard should tell a story or answer a question. (It should be meaningful to use logs).
- Dashboards should reduce cognitive load, not add to it. (It should be easy to fing information from logs, find erros or warnings).
- For fast dashboard creation we should use templates.
From https://grafana.com/docs/grafana/latest/best-practices/best-practices-for-creating-dashboards/.
