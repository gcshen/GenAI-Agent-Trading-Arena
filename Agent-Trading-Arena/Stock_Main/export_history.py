import argparse
import csv
import sqlite3
from pathlib import Path


def export_table(conn, table_name, output_dir):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    headers = [col[0] for col in cur.description]

    csv_path = output_dir / f"{table_name}.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    return headers, rows


def export_history(save_name: str):
    base = Path(__file__).resolve().parent
    save_dir = base / "save" / save_name
    db_path = save_dir / "data.db"
    if not db_path.exists():
        raise FileNotFoundError(f"data.db not found at {db_path}")

    conn = sqlite3.connect(db_path)

    tables = ["stock", "person", "account", "active_orders", "memory", "gossip"]
    output_dir = save_dir / "tables"
    output_dir.mkdir(exist_ok=True)

    markdown_lines = []
    markdown_lines.append(f"# Run History Summary: {save_name}\n")
    markdown_lines.append(f"- data.db: {db_path}")
    markdown_lines.append(f"- tables exported to: {output_dir}\n")

    for table in tables:
        headers, rows = export_table(conn, table, output_dir)
        markdown_lines.append(f"## {table} (rows: {len(rows)})")
        markdown_lines.append(f"Columns: {', '.join(headers)}")
        # show up to first 5 rows inline
        preview_rows = rows[:5]
        if preview_rows:
            markdown_lines.append("| " + " | ".join(headers) + " |")
            markdown_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
            for r in preview_rows:
                markdown_lines.append("| " + " | ".join(str(x) for x in r) + " |")
        else:
            markdown_lines.append("_no rows_")
        markdown_lines.append("")  # spacer

    md_path = save_dir / "run_history.md"
    with md_path.open("w") as f:
        f.write("\n".join(markdown_lines))

    print(f"Export complete.\n- Markdown: {md_path}\n- CSVs: {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Export run history to CSV and markdown.")
    parser.add_argument(
        "--save_name",
        type=str,
        default="sim_test_tmp",
        help="Name of the save folder under Stock_Main/save.",
    )
    args = parser.parse_args()
    export_history(args.save_name)


if __name__ == "__main__":
    main()
