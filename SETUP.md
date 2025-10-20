# Setup Guide

This guide will help you set up the notebooks project on your local machine.

## Step 1: Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

Check your Python version:
```bash
python --version
```

## Step 2: Clone the Repository

```bash
git clone https://github.com/TFG-yisuscc/notebooks.git
cd notebooks
```

## Step 3: Create a Virtual Environment

### On Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas, numpy (data processing)
- matplotlib, seaborn (visualization)
- scikit-learn (machine learning)
- jupyter, ipykernel, notebook (Jupyter environment)

## Step 5: Launch Jupyter

```bash
jupyter notebook
```

This will open Jupyter in your default web browser.

## Step 6: Start Working

1. Navigate to `notebooks/notebook_01/`
2. Open `notebook_01.ipynb`
3. Run the example cells to verify everything works

## Adding Your Data

1. Place your data files in the appropriate `dataset/` folder:
   - For notebook_01: `notebooks/notebook_01/dataset/`
   - For notebook_02: `notebooks/notebook_02/dataset/`
   - etc.

2. Update the notebook to load your data:
```python
from common.lib import utils, data_processing

dataset_path = utils.get_dataset_path('notebook_01')
df = data_processing.load_csv_data(dataset_path / 'your_file.csv')
```

## Troubleshooting

### Issue: Module not found

Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Can't import common libraries

Ensure the path setup in your notebook is correct:
```python
import sys
from pathlib import Path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))
```

### Issue: Jupyter kernel not found

Install the IPython kernel:
```bash
python -m ipykernel install --user
```

## Next Steps

- Read the main README.md for project structure
- Check out the example notebook_01 for usage examples
- Add your own notebooks following the established structure
- Explore the common libraries in `common/lib/`

## Support

If you encounter any issues, please:
1. Check this guide
2. Review the main README.md
3. Open an issue on GitHub
