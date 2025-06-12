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


@dataclass
class DataTransformationConfig:
    root_dir: Path
    df_output_path :  Path
    tranformed_data: Path


@dataclass
class ModelEvalutionConfig:
    root_dir: Path
    model_path :  Path
    tokenizer_path: Path
    prediction_results : Path