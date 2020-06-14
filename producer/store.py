import os
import requests
import logging

def store_metrics(metrics, timestamp, method, simulation_id):
    if method == 'disk':
        fn = f'data/{simulation_id}'

        if not os.path.exists('data'):
            os.mkdir('data')

        if not os.path.exists(fn):
            open(fn, 'a').close()

        with open(f'data/{simulation_id}', 'a') as f:
            f.write(f'{timestamp}, {metrics["height"]}, {metrics["speed"]}\n')

    if method == 'http':

        url = os.getenv('METRICS_URL', 'http://localhost:3000')

        res = requests.post(
            f'{url}/api/v1/metrics', 
            json={
                'height': metrics['height'],
                'speed': metrics['speed'],
                'time': str(timestamp),
                'simulation_id': str(simulation_id)
            }
        )

        logging.info(f'posted to metrics :: {res}')
