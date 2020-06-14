// Update with your config settings.

module.exports = {

  client: 'postgresql',
  connection: {
    database: process.env.POSTGRES_DB || 'db',
    user:     process.env.POSTGRES_USER || 'username',
    host:     process.env.POSTGRES_HOST || 'localhost',
    password: process.env.POSTGRES_PASSWORD || 'pass',
  },

};
