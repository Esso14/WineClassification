
from datetime import datetime
from pathlib import Path
from logger import logger, success


class FileManager:

    #--- Function don't need neither self nor cls ---
    @staticmethod
    def create_folder_with_timestamp(prefix: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

        folder_name = f"{prefix}_{timestamp}"

        try:
            path = Path("data") / folder_name
            path.mkdir(parents=True, exist_ok=True)
            success(f"The folder {path} was created successfully.")

            return str(path)
        
        except FileExistsError:
            logger.info(f"The folder {path} exists already.")
            
            return str(path)
