module.exports = {
  entry: [
      './client/static/js/index.jsx'
  ],
  module: {
      rules: [
          {
              test: /\.(js|jsx)$/,
              exclude: /node_modules/,
              use: ['babel-loader']
          }
      ]
  },
  output: {
      path: __dirname + '/client/static',
      filename: 'bundle.js'
  }
};