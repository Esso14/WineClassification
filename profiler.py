import os
from pathlib import Path
import pandas as pd
from config import ConfigManager
from utils import FileManager
from logger import logger, success
from datetime import datetime
from ydata_profiling import ProfileReport

os.chdir(Path(__file__).parent)

class DataProfiler:
    def __init__(self, data_):
        self.data = data_
        self.df = None
        self.df_info = None
        self.df_statistics = None

        self.config = ConfigManager("config/config.json")

        self.data_path = (
            FileManager.create_folder_with_timestamp(
                self.config.get("data_folder_prefix")
            )
        )

    #----- Generate CSV-file ---------------
    def generate_df_csv(self):
    
        file_path = Path(self.data_path) / "df_file.csv"

        self.df = pd.DataFrame(self.data.data, columns=self.data.feature_names)
        self.df["target"]=self.data.target

        self.df.to_csv(file_path, index=False)
        df_data = self.df.drop(columns=["target"])
        df_target = self.df.target
        success("CSV file was generated and saved successfully")
        return self.df, df_data, df_target
    
    #---- Generate REPORT --------
    def generate_report(self):

        self.get_infos()
        status = self.write_profile()

        if status:
            success("Report file generated successfully!")
        else:
            logger.error("Some error happened by generating Report-File !")

    
    #--- Get informations about the CSV-file ------
    def get_infos(self):
        num_rows, num_columns = self.df.shape

        column_datatypes = self.df.dtypes

        self.df_info = {
            "num_columns": num_columns,
            "num_rows": num_rows,
            "column_datatypes": column_datatypes,
            "num_duplicates": self.df.duplicated().sum(),
            "nan_values_per_column": self.df.isnull().sum()
        }

        self.df_statistics = {
            'Mean_value': self.df.mean(),
            'Median': self.df.median(),
            'Minimum': self.df.min(),
            'Maximum': self.df.max(),
            'Standard_deviation': self.df.std()
        }

    #--- SAVE profile report -----
    def write_profile(self):

        report_path = Path(self.data_path) / "profile_report.txt"

        with open(report_path, mode="w", encoding="UTF-8") as file:
            file.write("\nManually Report about Wine-Dataset\n")
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"\n{date_now}\n")
            file.write(35 * "-")

            file.write(f"\nNumber of columns: {self.df_info['num_columns']}")
            file.write(f"\nNumber of rows: {self.df_info['num_rows']}")
            file.write(f"\nNumber of duplicated rows: {self.df_info['num_duplicates']}")

            file.write("\n\nData types:\n")
            file.write(35 * "-")
            file.write("\n")
            file.write(str(self.df_info['column_datatypes']))

            file.write("\n\nNAN Values per column\n")
            file.write(35 * "-")
            for col, val in self.df_info['nan_values_per_column'].items():
                file.write(f"\n{col}: {val}")

            file.write("\n\nStatistics:\n")
            file.write(35 * "-")
            for col, val in self.df_statistics.items():
                file.write(f"\n{col}:\n--------\n{val}\n")

            return True

    #--------------------------------------------------------#
    #  Generate EDA (Explorative Data Analysis) automaticaly #
    #   with ProfileReport from ydata_profiling library.     #
    #--------------------------------------------------------#
    def create_profile(self):

        profile_path = Path(self.data_path) / "profile.html"
        
        profile = ProfileReport(self.df, title="Profile")
        profile.to_file(output_file=profile_path)
        success("Profile file successfully generate!")

    