import argparse
import logging
import uuid
import datetime
import time

from metrics import fetch_metrics
from store import store_metrics

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--takeoff-interval', required=True)
parser.add_argument('-d', '--duration', required=True)
parser.add_argument('-c', '--height-coefficient', required=True)
parser.add_argument('-s', '--takeoff-speed', required=True)
parser.add_argument('-v', '--speed-variance', required=True)
parser.add_argument('-i', '--interval', required=True)
parser.add_argument('-sm', '--storage-method', default='disk')

args = parser.parse_args()

takeoff_interval = int(args.takeoff_interval)
duration = int(args.duration)
height_coeff = float(args.height_coefficient)
takeoff_speed = float(args.takeoff_speed)
speed_var = float(args.speed_variance)
interval = float(args.interval)
storage_method = args.storage_method

logging.basicConfig(level=logging.DEBUG)

def main():

    simulation_id = uuid.uuid1()

    logging.info(f'Initialising Sim :: {simulation_id}')
    logging.info(f'Duration: {duration}')
    logging.info(f'Takeoff Interval: {takeoff_interval}')
    logging.info(f'Takeoff Speed: {takeoff_speed}')
    logging.info(f'Speed Var: {speed_var}')
    logging.info(f'Height Coeff: {height_coeff}')

    x = 0
    while x < duration:

        logging.info(f'simulation it :: {x}')
        metrics = fetch_metrics(x, duration, takeoff_interval, takeoff_speed, speed_var, height_coeff)
        timestamp = datetime.datetime.utcnow()
        logging.info(f'metrics :: {timestamp} :: height :: {metrics["height"]} :: speed :: {metrics["speed"]}')
        store_metrics(metrics, timestamp, storage_method, simulation_id)
        time.sleep(interval)
        x += 1

if __name__ == '__main__':
    main()