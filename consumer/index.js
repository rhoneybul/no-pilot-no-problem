const express = require('express')
const morgan = require('morgan')
const bodyParser = require('body-parser')

const {
  successResponse
} = require('./helpers');
const logger = require('./logger')

const app = express();

app.use(bodyParser.json());

const router = express.Router()

router.use('/', (_, res) => {
  return successResponse(res, 'noPilot noProblem API >>');
})

app.use(morgan('combined'));

const port = process.env.PORT || 3000;

app.listen(port, () => {
  logger.info({port}, 'app listening')
})