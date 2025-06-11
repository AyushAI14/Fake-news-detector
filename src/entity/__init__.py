from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_path: str
    local_file_dir: Path
    fake_data: Path
    true_data:Path
    df_output_path:Path


