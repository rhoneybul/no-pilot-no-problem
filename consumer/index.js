const express = require('express')
const morgan = require('morgan')
const bodyParser = require('body-parser')

const {
  successResponse
} = require('./helpers');
const logger = require('./logger')
const {
  createMetric 
} = require('./controllers')

const app = express();

app.use(bodyParser.json());

const router = express.Router()

router.get('/', (_, res) => {
  return successResponse(res, 'noPilot noProblem API >>');
})

router.post('/metrics', createMetric);

app.use(morgan('combined'));

app.use('/api/v1', router);

const port = process.env.PORT || 3000;

app.listen(port, () => {
  logger.info({port}, 'app listening')
})