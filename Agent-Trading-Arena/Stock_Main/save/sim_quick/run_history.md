# Run History Summary: sim_quick

- data.db: /Users/halamadrid/Desktop/DROM B9153 Generative AI Technical and Social/Project/GenAI-Agent-Trading-Arena/Agent-Trading-Arena/Stock_Main/save/sim_quick/data.db
- tables exported to: /Users/halamadrid/Desktop/DROM B9153 Generative AI Technical and Social/Project/GenAI-Agent-Trading-Arena/Agent-Trading-Arena/Stock_Main/save/sim_quick/tables

## stock (rows: 20)
Columns: stock_id, virtual_date, weekday, volume, quantity, last_price, begin_price, highest_price, lowest_price
| stock_id | virtual_date | weekday | volume | quantity | last_price | begin_price | highest_price | lowest_price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | -4 | 0 | 0 | 0 | 110 | 110 | 110 | 110 |
| 0 | -3 | 0 | 0 | 0 | 130 | 130 | 130 | 130 |
| 0 | -2 | 0 | 0 | 0 | 90 | 90 | 90 | 90 |
| 0 | -1 | 0 | 0 | 0 | 160 | 160 | 160 | 160 |
| 0 | 0 | 0 | 0 | 0 | 180 | 180 | 180 | 180 |

## person (rows: 6)
Columns: person_id, virtual_date, cash, asset, wealth, work_income, capital_gain, daily_expense, principle
| person_id | virtual_date | cash | asset | wealth | work_income | capital_gain | daily_expense | principle |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -1 | 0 | 0 | 105000 | 105000 | 0 | 0 | 0 | NA |
| 0 | 0 | 39295.22727272727 | 707.6999999999999 | 40002.92727272727 | 500 | 2.950000000000017 | 60 | conservative |
| 1 | 0 | 29433.832167832166 | 566.16 | 29999.99216783217 | 400 | 0 | 80 | radical |
| 0 | 1 | 38547.868727272726 | 707.6999999999999 | 39255.56872727272 | 500 | 2.950000000000017 | 862.3585454545454 | conservative |
| 1 | 1 | 28843.992324475523 | 566.16 | 29410.152324475523 | 400 | 0 | 681.8398433566433 | radical |

## account (rows: 10)
Columns: person_id, stock_id, virtual_date, weekday, quantity, cost_price, current_price, profit, start_date
| person_id | stock_id | virtual_date | weekday | quantity | cost_price | current_price | profit | start_date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -1 | 0 | 0 | 0 | 150 | 0 | 180 | 0 | 0 |
| -1 | 1 | 0 | 0 | 191 | 0 | 140 | 0 | 0 |
| -1 | 2 | 0 | 0 | 250 | 0 | 200 | 0 | 0 |
| 0 | 1 | 0 | 0 | 5 | 140.95454545454547 | 141.54 | 0.004185881518268915 | 0 |
| 1 | 1 | 0 | 0 | 4 | 141.54195804195805 | 141.54 | 0 | 0 |

## active_orders (rows: 7)
Columns: timestamp, virtual_date, weekday, iteration, stock_id, person_id, type, price, quantity, status
| timestamp | virtual_date | weekday | iteration | stock_id | person_id | type | price | quantity | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1764505393995 | 0 | 0 | 0 | 0 | -1 | sell | 180 | 150 | closed |
| 1764505394008 | 0 | 0 | 0 | 1 | -1 | sell | 140 | 191 | closed |
| 1764505394021 | 0 | 0 | 0 | 2 | -1 | sell | 200 | 250 | closed |
| 1764505394040 | 0 | 0 | 0 | 1 | 1 | buy | 147 | 4 | finished |
| 1764505394053 | 0 | 0 | 0 | 1 | 0 | buy | 147 | 5 | finished |

## memory (rows: 2)
Columns: person_id, virtual_date, iteration, stock_operations, strategy, type, gossip, analysis_for_stocks, analysis_for_strategy, stock_prices, market_change, financial_situation
| person_id | virtual_date | iteration | stock_operations | strategy | type | gossip | analysis_for_stocks | analysis_for_strategy | stock_prices | market_change | financial_situation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | buy 5 shares of stock B at $140.0 | conservative | buy | None | The analysis results:
- hold
- hold
- hold | None | 
    - A:
        - The closing prices in the past 5 days are: [110, 130, 90, 160, 180]
        - Dividend per share: $22
        - Current price change: +0.00%, Current price: $180.0
        - Intraday High：$180
        - Intraday Low: $180
        - Intraday Mean: $180.0

    - B:
        - The closing prices in the past 5 days are: [80, 95, 70, 115, 140]
        - Dividend per share: $23
        - Current price change: +0.00%, Current price: $140.0
        - Intraday High：$140
        - Intraday Low: $140
        - Intraday Mean: $140.0

    - C:
        - The closing prices in the past 5 days are: [220, 190, 210, 180, 200]
        - Dividend per share: $25
        - Current price change: +0.00%, Current price: $200.0
        - Intraday High：$200
        - Intraday Low: $200
        - Intraday Mean: $200.0
 | Current market index change: 0.00% | Your total portfolio balance is $0.00, you do not hold any stock right now. |
| 1 | 0 | 0 | buy 4 shares of stock B at $140.0 | radical | buy | None | The analysis results:
- hold
- hold
- hold | None | 
    - A:
        - The closing prices in the past 5 days are: [110, 130, 90, 160, 180]
        - Dividend per share: $22
        - Current price change: +0.00%, Current price: $180.0
        - Intraday High：$180
        - Intraday Low: $180
        - Intraday Mean: $180.0

    - B:
        - The closing prices in the past 5 days are: [80, 95, 70, 115, 140]
        - Dividend per share: $23
        - Current price change: +0.00%, Current price: $140.0
        - Intraday High：$140
        - Intraday Low: $140
        - Intraday Mean: $140.0

    - C:
        - The closing prices in the past 5 days are: [220, 190, 210, 180, 200]
        - Dividend per share: $25
        - Current price change: +0.00%, Current price: $200.0
        - Intraday High：$200
        - Intraday Low: $200
        - Intraday Mean: $200.0
 | Current market index change: 0.00% | Your total portfolio balance is $0.00, you do not hold any stock right now. |

## gossip (rows: 2)
Columns: person_id, virtual_date, gossip
| person_id | virtual_date | gossip |
| --- | --- | --- |
| 0 | 0 | None |
| 1 | 0 | None |
