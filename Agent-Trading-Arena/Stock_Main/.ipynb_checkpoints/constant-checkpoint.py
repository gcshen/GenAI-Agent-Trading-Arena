import time
import os
import os.path as osp

current_milli_time = lambda: int(round(time.time() * 1000))


FORMAT = "%Y-%m-%d%H:%M:%S"
STOCK_NAMES = ["0", "1", "2", "3", "4"]

Daily_Price_Limit = 0.7
expense_ratio = 0.03
Fluctuation_Constant = 20.0
verbose = False

# Simulation parameters
Iterations_Daily = 3
No_Days = 3
Num_Person = 9
Num_Stock = 3
SAVE_NAME = "sim01"
persona_name = "persona.json"
stock_name = "stocks.json"
Save_Path = osp.join("./save", SAVE_NAME)


if not os.path.exists(Save_Path):
    os.makedirs(Save_Path)


persona_path = osp.join(Save_Path, "persona.json")
stock_path = osp.join(Save_Path, "stocks.json")

analysis_num = 3
gossip_num_max = 3
