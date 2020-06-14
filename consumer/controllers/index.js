const {
  successResponse,
  errorResponse
} = require('../helpers')

const createMetric = (req, res) => {
  
  try {
    let data = req.body;
    let metric = new Metric(data);
    return successResponse(res, 'successfully created metric', metric);
  } catch(e) {
    return errorResponse(res, e, { message: 'could not create metric', status_code: 500, })
  }
}

module.exports = {
  createMetric,
}