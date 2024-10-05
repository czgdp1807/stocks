# About

This respository contains code which computes your stock market portfolio for a given target amount. I use it for my own portfolio.

# Disclaimer

You can use it for yourself completely at your risk. I do not take any responsibility for the consequences of using the code in this repository. I am not a government certified stock market advisor. I am also not a stock market expert. I do not work for any trading firms. I have not worked at trading firms in the past as well.

Reiterating, feel free to use this repository but completely at your own risk. I do not take any responsibility and credits for the consequences of using this repository.

# How to use this repository?

1. We need a data file in JSON format. The JSON data file should be an array of JSON objects (key-value pairs). Let me explain the meaning of each key. You can refer `stocks_data.json`,

"name" - Name of the stock.

"pe" - P/E ratio.

"pb" - P/B ratio.

"price" - Current share price of the stock.

"market_value" - The current market value of your investment in this stock. In other words, value of your current holdings in this stock. If you haven't invested any amount yet, then set it `0`.

"shares" - Current number of shares you hold in this stock.

2. Set your target amount. By target amount I mean, what should be the final value of your portfolio. Say the market value of your portfolio is `x`. You want to invest an additional `y` amount. Then the target amount will be the sum of `x` and `y`, i.e., `x + y`. For example my portfolio size is `807736` and I want to invest `465545`. The target amount will be `1273281`.

3. Change your current working directory to this repository in command line interface/terminal.

4. Execute, `python stocks.py --target_amount=1273281 --path=stocks_data.json`.

5. The result will be saved in `portfolio.csv`. You can import it on Google sheets and do further modifications to it.

Read the disclaimer above before following the above steps.
