const logger = require('../logger');
const knex = require('../knex');

class Metric {

  constructor({
    time, 
    height, 
    speed, 
    device_id,
    simulation_id,
  }) {

    try {
      this.time = time;
      this.height = height;
      this.speed = speed;
      this.device_id = device_id;
      this.simulation_id = simulation_id;

      logger.info(this, 'created metric');
    } catch(e) {
      logger.error(e, 'could not create metric')
    }
    

  }

  async write () {
    logger.info(this, 'writing metric');
    try {
      await knex('flight_metrics').insert(this);
    } catch(e) {
      logger.error(e, 'failed writing metric');
    } 
    
  }

}

module.exports = { Metric, }