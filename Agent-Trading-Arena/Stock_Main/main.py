import argparse
import os, sys
import os.path as osp
import random
import time
import json
from pathlib import Path

PROJ_BASE = Path(__file__).resolve().parent.parent
print(f">>> PROJ_BASE: {str(PROJ_BASE)}\n") ##LOG
sys.path.insert(0, str(PROJ_BASE))

import _paths

def init_paths(**kwargs):
    _paths.PROJ_BASE = PROJ_BASE
    _paths.MAIN_PATH = PROJ_BASE.joinpath("Stock_Main")
    _paths.SAVE_PATH = PROJ_BASE.joinpath("Stock_Main/save")
    _paths.CONTENT_PATH = PROJ_BASE.joinpath("Stock_Main/content")
    _paths.PROMPT_PATH = _paths.CONTENT_PATH.joinpath("our_prompt_template")

from database_utils import query_all_stocks, Database_operate
from Person import Person, Broker
from Stock import Stock, Market_index
from Market import Market
from behavior import stock_ops, reflection, generate_gossip
from load_json import save_all, load_all

def get_args():
    parser = argparse.ArgumentParser(description='[Stock Simulation] Market Environment Settings')

    parser.add_argument('--Iterations_Daily', type=int, default=3, help='number of iterations per day')
    parser.add_argument('--No_Days', type=int, default=3, help='number of trading days')
    parser.add_argument('--Num_Person', type=int, default=9, help='number of agents')
    parser.add_argument('--Num_Stock', type=int, default=3, help='number of stocks')
    parser.add_argument('--SAVE_NAME', type=str, default='sim01', help='name of save folder')
    parser.add_argument('--STOCK_NAMES', type=str, nargs='+', default=["0", "1", "2", "3", "4"],
                    help='list of stock names (e.g., 0 1 2 3 4)')

    parser.add_argument('--persona_name', type=str, default='persona.json', help='filename for personas')
    parser.add_argument('--stock_name', type=str, default='stocks.json', help='filename for stocks')

    parser.add_argument('--Daily_Price_Limit', type=float, default=0.7, help='daily price change limit')
    parser.add_argument('--expense_ratio', type=float, default=0.03, help='capital cost rate')
    parser.add_argument('--Fluctuation_Constant', type=float, default=20.0, help='price fluctuation constant')
    parser.add_argument('--verbose', action='store_true', help='print debug information')

    parser.add_argument('--analysis_num', type=int, default=3, help='number of agents performing analysis')
    parser.add_argument('--gossip_num_max', type=int, default=3, help='maximum number of gossip entries per round')

    args = parser.parse_args()

    # Derived paths
    # args.Save_Path = osp.join("./save", args.SAVE_NAME)
    args.Save_Path = _paths.SAVE_PATH.joinpath(args.SAVE_NAME)
    # print(f"------ args.SAVE_NAME -------\n{args.SAVE_NAME}\n----------------------\n") ##LOG
    if not os.path.exists(args.Save_Path):
        os.makedirs(args.Save_Path)

    args.persona_path = osp.join(args.Save_Path, args.persona_name)
    args.stock_path = osp.join(args.Save_Path, args.stock_name)
    # print(f"------ args.stock_path -------\n{args.stock_path}\n------------------------------\n") ##LOG

    return args


def init_all(args, load=False):
    if load:
        (
            current_date,
            current_iteration,
            broker,
            market_index,
            market,
            stocks,
            persons,
        ) = load_all(args)
    else:
        database = Database_operate(osp.join(args.Save_Path, "data"))

        # Clear existing tables
        for table in ["active_orders", "stock", "person", "account", "memory", "gossip"]:
            cmd = f"drop table if exists {table}"
            database.execute_sql(cmd)

        database.init_database()

        stocks = [Stock(i, database, args.stock_path) for i in range(args.Num_Stock)]
        # print(stocks) ##LOG
        market_index = Market_index(stocks, database)
        broker = Broker(stocks, database)
        
        ### BUG: why append broker??? --------------------
        persons = [Person(i, broker, stocks, database, args.persona_path) for i in range(args.Num_Person)]
        persons.append(broker)
        ### ----------------------------------------------

        market = Market(broker, persons, stocks, database)

    return 0, 0, broker, market_index, market, stocks, persons


def overall_test(args):
    (
        current_date,
        current_iteration,
        broker,
        market_index,
        market,
        stocks,
        persons,
    ) = init_all(args, load=False)

    for virtual_date in range(args.No_Days):
        if virtual_date == 0:
            broker.ipo(virtual_date)

        market_index.update_market_index(virtual_date)
        generate_gossip(virtual_date, persons, stocks)

        for iter in range(args.Iterations_Daily):
            ops = stock_ops(virtual_date, persons, stocks, market_index, iter, args)
            rand = random.sample(range(0, args.Num_Person), args.Num_Person)
            for i in rand:
                for j in range(2): 
                    op = ops[i][j]
                    persons[i].create_order(i, op, virtual_date, iter)

            market.match_order(virtual_date, args)
            market.end_of_market(virtual_date, args)
            market_index.update_market_index(virtual_date)

            for each_person in persons:
                if each_person.person_id >= 0: ## NOTE: since broker.persion_id==-1 -> not a broker
                    each_person.end_of_iteration(virtual_date, iter)

            reflection(virtual_date, persons, stocks, market_index, iter)
            save_all(virtual_date, iter, stocks, market_index, persons, market, args)

        # End of the trading day
        market.end_of_day(virtual_date)
        for each_person in persons:
            if each_person.person_id >= 0: ## BUG (fixed): not a broker
                each_person.end_of_day(virtual_date, args)
            else:  ## BUG (fixed): a broker
                each_person.end_of_day(virtual_date)
        for each_stock in stocks:
            each_stock.end_of_day(virtual_date)
        market_index.end_of_day(virtual_date)


if __name__ == "__main__":
    init_paths()
    args = get_args()
    overall_test(args)
