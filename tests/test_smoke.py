import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
MAIN = REPO_ROOT / "Agent-Trading-Arena" / "Stock_Main" / "main.py"
EXPORT = REPO_ROOT / "Agent-Trading-Arena" / "Stock_Main" / "export_history.py"
SAVE_NAME = "test_smoke"
SAVE_DIR = REPO_ROOT / "Agent-Trading-Arena" / "Stock_Main" / "save" / SAVE_NAME


def _run(cmd, env=None):
    result = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    return result


def test_offline_simulation_runs():
    env = dict(**dict(os.environ))
    env["OFFLINE_MODE"] = "1"
    cmd = [
        sys.executable,
        str(MAIN),
        "--Iterations_Daily",
        "1",
        "--No_Days",
        "1",
        "--Num_Person",
        "2",
        "--Num_Stock",
        "3",
        "--SAVE_NAME",
        SAVE_NAME,
        "--persona_name",
        "persona.json",
        "--stock_name",
        "stocks.json",
        "--Daily_Price_Limit",
        "0.6",
        "--expense_ratio",
        "0.02",
        "--Fluctuation_Constant",
        "15.0",
        "--analysis_num",
        "1",
        "--gossip_num_max",
        "0",
    ]
    result = _run(cmd, env)
    assert result.returncode == 0, result.stderr
    assert (SAVE_DIR / "data.db").exists()


def test_export_history_runs():
    # depends on prior smoke run creating SAVE_DIR
    if not (SAVE_DIR / "data.db").exists():
        test_offline_simulation_runs()
    env = dict(**dict(os.environ))
    env["OFFLINE_MODE"] = "1"
    cmd = [sys.executable, str(EXPORT), "--save_name", SAVE_NAME]
    result = _run(cmd, env)
    assert result.returncode == 0, result.stderr
    assert (SAVE_DIR / "run_history.md").exists()
    assert (SAVE_DIR / "summary.json").exists()
