import os

def store_metrics(metrics, timestamp, method, simulation_id):
    if method == 'disk':
        fn = f'data/{simulation_id}'

        if not os.path.exists('data'):
            os.mkdir('data')

        if not os.path.exists(fn):
            open(fn, 'a').close()

        with open(f'data/{simulation_id}', 'a') as f:
            f.write(f'{timestamp}, {metrics["height"]}, {metrics["speed"]}\n')
