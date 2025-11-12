import os
from pathlib import Path
from MyProject.logging import logger
from MyProject.entity import DataValidationConfig




import os
from MyProject.logging import logger
from MyProject.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    
    def validate_all_files_exist(self)-> bool:
        try:
            # prefer extracted path which contains the dataset folder
            extracted_dataset_dir = os.path.join("artifacts","data_ingestion","extracted_data","samsum_dataset")
            fallback_dataset_dir = os.path.join("artifacts","data_ingestion","samsum_dataset")
            target_dir = extracted_dataset_dir if os.path.isdir(extracted_dataset_dir) else fallback_dataset_dir

            if not os.path.isdir(target_dir):
                raise FileNotFoundError(f"Dataset directory not found at {target_dir}")

            present_items = set(os.listdir(target_dir))
            required_items = set(self.config.ALL_REQUIRED_FILES)
            missing = [name for name in required_items if name not in present_items]

            validation_status = len(missing) == 0
            with open(self.config.STATUS_FILE, 'w') as f:
                if validation_status:
                    f.write(f"Validation status: True")
                else:
                    f.write(f"Validation status: False; Missing: {', '.join(missing)}")

            if validation_status:
                logger.info(f"Validation succeeded. Found all required items in {target_dir}")
            else:
                logger.error(f"Validation failed. Missing items: {missing} in {target_dir}")

            return validation_status
        
        except Exception as e:
            raise e