# Project Structure Overview

This document provides a visual overview of the project structure and workflow.

## Directory Tree

```
notebooks/
├── .gitignore                          # Git ignore rules
├── README.md                           # Main project documentation
├── SETUP.md                            # Setup and installation guide
├── ADDING_NOTEBOOKS.md                 # Guide for adding new notebooks
├── requirements.txt                    # Python dependencies
│
├── common/                             # Shared resources
│   ├── README.md                       # Common libraries documentation
│   ├── config/                         # Configuration files
│   │   └── config.json                 # Project-wide settings
│   └── lib/                            # Shared Python modules
│       ├── __init__.py                 # Library initialization
│       ├── data_processing.py          # Data utilities
│       ├── visualization.py            # Plotting utilities
│       └── utils.py                    # General utilities
│
└── notebooks/                          # Individual notebook projects
    ├── notebook_01/                    # Example notebook
    │   ├── README.md                   # Notebook documentation
    │   ├── notebook_01.ipynb           # Jupyter notebook
    │   └── dataset/                    # Notebook-specific data
    │       └── README.md
    ├── notebook_02/                    # Template notebook
    │   ├── README.md
    │   ├── notebook_02.ipynb
    │   └── dataset/
    │       └── README.md
    └── notebook_03/                    # Template notebook
        ├── README.md
        ├── notebook_03.ipynb
        └── dataset/
            └── README.md
```

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     User/Developer                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   Clone Repository     │
         │   Install Dependencies │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   Choose/Create        │
         │   Notebook             │
         └────────────┬───────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
  ┌───────────────┐      ┌──────────────────┐
  │ Use Existing  │      │  Create New      │
  │ Notebook      │      │  Notebook        │
  └───────┬───────┘      └────────┬─────────┘
          │                       │
          │                       ▼
          │              ┌──────────────────┐
          │              │ mkdir notebook_XX │
          │              │ Add README.md     │
          │              │ Create .ipynb     │
          │              └────────┬─────────┘
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │  Add Dataset Files     │
         │  to dataset/ folder    │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │  Import Common Libs    │
         │  - data_processing     │
         │  - visualization       │
         │  - utils               │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │  Perform Analysis      │
         │  - Load data           │
         │  - Process data        │
         │  - Visualize           │
         │  - Save results        │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │  Document Results      │
         │  in Notebook           │
         └────────────────────────┘
```

## Data Flow

```
┌──────────────┐
│ Dataset File │
│  (.csv, etc) │
└──────┬───────┘
       │
       ▼
┌────────────────────────┐
│ notebook_XX/dataset/   │ ◄─── Store raw data here
└──────┬─────────────────┘
       │
       ▼
┌────────────────────────┐
│ Load with Common Libs  │
│ data_processing.       │
│ load_csv_data()        │
└──────┬─────────────────┘
       │
       ▼
┌────────────────────────┐
│ Process Data           │
│ - Clean missing values │
│ - Normalize            │
│ - Transform            │
└──────┬─────────────────┘
       │
       ▼
┌────────────────────────┐
│ Visualize              │
│ - Distributions        │
│ - Correlations         │
│ - Trends               │
└──────┬─────────────────┘
       │
       ▼
┌────────────────────────┐
│ Save Results           │
│ Back to dataset/       │
└────────────────────────┘
```

## Library Import Pattern

Every notebook follows this pattern:

```python
# 1. Add project root to Python path
import sys
from pathlib import Path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))

# 2. Import common libraries
from common.lib import data_processing, visualization, utils

# 3. Import standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 4. Get configuration and paths
config = utils.load_config()
dataset_path = utils.get_dataset_path('notebook_XX')
```

## Key Features

### 1. Common Libraries
- **Centralized utilities**: All notebooks share the same functions
- **Easy to maintain**: Update once, applies to all notebooks
- **Consistent style**: All visualizations follow the same theme

### 2. Individual Datasets
- **Isolation**: Each notebook has its own data folder
- **Organization**: Easy to manage notebook-specific data
- **Portability**: Each notebook is self-contained

### 3. Configuration Management
- **Global settings**: Project-wide configuration in `common/config/config.json`
- **Easy updates**: Change settings in one place
- **Version control**: Configuration is tracked in git

### 4. Documentation
- **Project level**: README.md, SETUP.md
- **Notebook level**: Each notebook has its own README
- **Component level**: Common libraries documented
- **How-to guides**: ADDING_NOTEBOOKS.md for extensions

## Usage Examples

### Loading Data
```python
from common.lib import utils, data_processing

dataset_path = utils.get_dataset_path('notebook_01')
df = data_processing.load_csv_data(dataset_path / 'data.csv')
```

### Cleaning Data
```python
# Remove rows with missing values
cleaned_df = data_processing.clean_missing_values(df, strategy='drop')

# Or fill missing values
filled_df = data_processing.clean_missing_values(df, strategy='fill', fill_value=0)
```

### Visualization
```python
from common.lib import visualization

# Plot distribution
visualization.plot_distribution(df['column'], title='Distribution')

# Plot correlation matrix
visualization.plot_correlation_matrix(df, title='Correlations')
```

### Configuration
```python
from common.lib import utils

# Load configuration
config = utils.load_config()
random_seed = config['common_settings']['random_seed']

# Save configuration
new_config = {'key': 'value'}
utils.save_config(new_config, 'my_config.json')
```

## Extension Points

1. **Add new common functions**: Edit files in `common/lib/`
2. **Add new notebooks**: Follow `ADDING_NOTEBOOKS.md` guide
3. **Add new dependencies**: Update `requirements.txt`
4. **Add new configurations**: Edit `common/config/config.json`

## Benefits

✅ **Maintainable**: Common code in one place  
✅ **Organized**: Clear structure for notebooks and data  
✅ **Scalable**: Easy to add new notebooks  
✅ **Documented**: Comprehensive documentation  
✅ **Reusable**: Shared utilities across all notebooks  
✅ **Consistent**: Same style and patterns throughout
