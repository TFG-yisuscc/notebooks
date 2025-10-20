# Dataset Directory

This directory is for storing dataset files for this notebook.

## Usage
- Place your CSV, Excel, JSON, or other data files here
- The notebook can access these files using the common utilities

## Example
```python
from common.lib import utils

# Get dataset path
dataset_path = utils.get_dataset_path('notebook_01')

# Load a file
data_file = dataset_path / 'my_data.csv'
```

## Notes
- Keep data files organized
- Consider using descriptive filenames
- Document your datasets in this README if needed
