"""
General utility functions for all notebooks.
"""
import os
import json
from pathlib import Path
from typing import Dict, Any


def get_project_root() -> Path:
    """
    Get the root directory of the project.
    
    Returns:
        Path: Project root directory
    """
    return Path(__file__).parent.parent.parent


def get_dataset_path(notebook_name: str) -> Path:
    """
    Get the dataset directory path for a specific notebook.
    
    Args:
        notebook_name: Name of the notebook (e.g., 'notebook_01')
        
    Returns:
        Path: Path to the notebook's dataset directory
    """
    return get_project_root() / "notebooks" / notebook_name / "dataset"


def load_config(config_name: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from the common config directory.
    
    Args:
        config_name: Name of the configuration file
        
    Returns:
        Dict: Configuration dictionary
    """
    config_path = get_project_root() / "common" / "config" / config_name
    
    if not config_path.exists():
        return {}
    
    with open(config_path, 'r') as f:
        return json.load(f)


def save_config(config: Dict[str, Any], config_name: str = "config.json") -> None:
    """
    Save configuration to the common config directory.
    
    Args:
        config: Configuration dictionary
        config_name: Name of the configuration file
    """
    config_path = get_project_root() / "common" / "config" / config_name
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)


def ensure_directory(path: Path) -> None:
    """
    Ensure a directory exists, create if it doesn't.
    
    Args:
        path: Directory path
    """
    path.mkdir(parents=True, exist_ok=True)
