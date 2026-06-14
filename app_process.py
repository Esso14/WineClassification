
from sklearn.datasets import load_wine
import argparse
from colorama import Fore, Style
from logger import logger
from profiler import DataProfiler
from processing import DataProcess

wine_data = load_wine()
data_profiler = DataProfiler(wine_data)
data_process = DataProcess(wine_data)

def create_cli():
    parser = argparse.ArgumentParser(
        description=f"{Fore.CYAN}Wice Classification CLI{Style.RESET_ALL}"
    )

    subparsers = parser.add_subparsers(dest="command")

    # --- generate CSV-file ------
    subparsers.add_parser(
        "generate-csv", 
        help="Generate and save csv file with pandas DataFrame"
    )

    # --- generate and profile CSV-file ------
    subparsers.add_parser(
        "profile-csv", 
        help="Generate and save file report"
    )

 # --- Fit and save best model ------
    subparsers.add_parser(
        "fit-model", 
        help="Fit und save de best model"
    )

# --- Fit and save best model ------
    subparsers.add_parser(
        "best-model", 
        help="Fit und save de best model after csv-report"
    )

    return parser

def main():
    parser = create_cli()
    args = parser.parse_args()

    if args.command == "generate-csv":
        data_profiler.generate_df_csv()

    if args.command == "profile-csv":
        data_profiler.generate_df_csv()
        data_profiler.generate_report()
        data_profiler.create_profile()

    if args.command == "best-model":
        data_profiler.generate_df_csv()
        data_profiler.generate_report()
        data_profiler.create_profile()
        data_process.processing()

if __name__ == "__main__":
    main()        
