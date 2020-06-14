const successResponse = (res, message) => {

  res.status(200)
  return res.send({
    message,
    status,
    status_code: 200, 
  })

} 

module.exports = { successResponse, };