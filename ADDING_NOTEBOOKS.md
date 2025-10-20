# Adding a New Notebook

This guide shows you how to add a new notebook to the project.

## Quick Steps

1. **Create the notebook folder structure:**
```bash
# Replace 'notebook_04' with your desired name
mkdir -p notebooks/notebook_04/dataset
```

2. **Create a README for your notebook:**
```bash
cat > notebooks/notebook_04/README.md << 'EOF'
# Notebook 04: [Your Title]

## Description
[Describe what this notebook does]

## Dataset
Place your dataset files in the `dataset/` folder.

## Usage
1. Add data files to `dataset/`
2. Open `notebook_04.ipynb`
3. Run your analysis
EOF
```

3. **Create a README for the dataset folder:**
```bash
cat > notebooks/notebook_04/dataset/README.md << 'EOF'
# Dataset Directory

Place your dataset files for notebook_04 here.
EOF
```

4. **Start Jupyter and create your notebook:**
```bash
cd notebooks/notebook_04
jupyter notebook
```

5. **In Jupyter, create a new Python 3 notebook and save it as `notebook_04.ipynb`**

6. **Add the standard imports to your notebook:**
```python
# Cell 1: Setup imports
import sys
from pathlib import Path

# Add common library to path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))

# Import common libraries
from common.lib import data_processing, visualization, utils

# Cell 2: Standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cell 3: Get dataset path
dataset_path = utils.get_dataset_path('notebook_04')
print(f"Dataset path: {dataset_path}")

# Cell 4: Load configuration
config = utils.load_config()
print("Project configuration:", config)
```

## Notebook Template

Here's a basic template for your notebook:

### Cell 1: Title and Description
```markdown
# Notebook 04: [Your Title]

Description of your analysis.
```

### Cell 2: Imports
```python
import sys
from pathlib import Path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))

from common.lib import data_processing, visualization, utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Cell 3: Configuration
```python
config = utils.load_config()
dataset_path = utils.get_dataset_path('notebook_04')
```

### Cell 4: Load Your Data
```python
# Load your data
data_file = dataset_path / 'your_data.csv'
df = data_processing.load_csv_data(data_file)
df.head()
```

### Cell 5+: Your Analysis
Add cells for your specific analysis.

## Tips

- Keep notebook names consistent: `notebook_XX` where XX is a number
- Document your work with markdown cells
- Use the common libraries to avoid code duplication
- Save processed data back to the `dataset/` folder if needed
- Update the notebook's README.md with specifics about your analysis

## Common Libraries Available

- **data_processing**: Load, clean, and process data
- **visualization**: Create plots and visualizations
- **utils**: Path helpers and configuration management

See `common/README.md` for detailed documentation of available functions.
