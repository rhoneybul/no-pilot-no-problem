import logger from '../logger';

class Metric {

  constructor({
    timestamp, 
    height, 
    speed, 
    device_id,
    simulation_id,
  }) {

    this.timestamp = timestamp;
    this.height = height;
    this.speed = speed;
    this.device_id = device_id;
    this.simulation_id = simulation_id;

    logger.info(this, 'created metric');

  }

  write() {
    logger.info(this, 'writing metric');
  }

}