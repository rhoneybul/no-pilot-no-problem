const {
  Metric
} = require('../models/index')

const {
  successResponse,
  errorResponse
} = require('../helpers')

const createMetric = async (req, res) => {
  
  try {
    let data = req.body;
    let metric = new Metric(data);
    metric.write();
    return successResponse(res, 'successfully created metric', metric);
  } catch(e) {
    return errorResponse(res, e, { message: 'could not create metric', status_code: 500, })
  }
}

module.exports = {
  createMetric,
}