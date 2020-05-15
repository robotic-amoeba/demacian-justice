module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      }, {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }, {
        test: /\.s[ac]ss$/i,
        use: ["style-loader", "css-loader", "sass-loader"]
      }, {
          test: /\.(png|jpe?g|gif)$/i,
          use: [
            {
              loader: 'url-loader',
            },
          ]
        },

    ]
  }
};
