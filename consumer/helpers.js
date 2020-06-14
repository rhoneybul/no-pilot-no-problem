const successResponse = (res, message, data, status) => {

  status = status || 'success'

  res.status(200)
  return res.send({
    message,
    status,
    status_code: 200, 
    data,
  })

} 

const errorResponse = (res, e, {message, status_code}) => {

  status_code = status_code || 500;
  message = message || 'error';

  res.status(status_code)
  return res.send({
    message, 
    status_code,
    status: 'error',
    e,
  })

}

module.exports = { successResponse, errorResponse, };