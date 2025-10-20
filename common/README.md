# Common Libraries

This directory contains shared libraries and utilities used across all notebooks in the project.

## Structure

- `lib/`: Python modules with reusable functions
  - `__init__.py`: Library initialization
  - `data_processing.py`: Data manipulation and cleaning utilities
  - `visualization.py`: Plotting and visualization functions
  - `utils.py`: General utility functions

- `config/`: Configuration files
  - `config.json`: Project-wide configuration settings

## Usage

All notebooks can import these libraries by adding the project root to their Python path:

```python
import sys
from pathlib import Path

# Add common library to path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))

# Import common libraries
from common.lib import data_processing, visualization, utils
```

## Available Functions

### data_processing.py
- `load_csv_data()`: Load CSV files with common preprocessing
- `clean_missing_values()`: Handle missing values
- `normalize_column()`: Normalize data to 0-1 range
- `get_basic_stats()`: Get statistical descriptions

### visualization.py
- `plot_distribution()`: Plot histograms
- `plot_correlation_matrix()`: Plot correlation heatmaps
- `plot_scatter()`: Create scatter plots
- `plot_time_series()`: Plot time series data

### utils.py
- `get_project_root()`: Get project root directory
- `get_dataset_path()`: Get dataset path for a notebook
- `load_config()`: Load configuration files
- `save_config()`: Save configuration files
- `ensure_directory()`: Create directories if they don't exist

## Adding New Functions

To add new shared functionality:

1. Add your function to the appropriate module in `lib/`
2. Document it with a docstring
3. Import it in your notebooks as shown above
