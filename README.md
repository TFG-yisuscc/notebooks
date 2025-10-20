# Notebooks Project

A structured multi-notebook project with shared libraries and individual dataset management.

## 📁 Project Structure

```
notebooks/
├── common/                      # Shared libraries and configurations
│   ├── lib/                    # Common Python modules
│   │   ├── __init__.py
│   │   ├── data_processing.py  # Data manipulation utilities
│   │   ├── visualization.py    # Plotting and visualization
│   │   └── utils.py           # General utilities
│   └── config/                 # Configuration files
│       └── config.json         # Project configuration
├── notebooks/                   # Individual notebook projects
│   ├── notebook_01/            # Example notebook 1
│   │   ├── dataset/           # Dataset folder for notebook 1
│   │   ├── notebook_01.ipynb  # Jupyter notebook
│   │   └── README.md
│   ├── notebook_02/            # Example notebook 2
│   │   ├── dataset/           # Dataset folder for notebook 2
│   │   ├── notebook_02.ipynb
│   │   └── README.md
│   └── notebook_03/            # Example notebook 3
│       ├── dataset/           # Dataset folder for notebook 3
│       ├── notebook_03.ipynb
│       └── README.md
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TFG-yisuscc/notebooks.git
cd notebooks
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start Jupyter:
```bash
jupyter notebook
```

## 📚 Usage

### Working with Notebooks

1. Navigate to a specific notebook folder (e.g., `notebooks/notebook_01/`)
2. Place your dataset files in the `dataset/` subfolder
3. Open the `.ipynb` file in Jupyter
4. Run the cells to perform your analysis

### Using Common Libraries

All notebooks can access the shared libraries in the `common/` directory:

```python
import sys
from pathlib import Path

# Add common library to path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))

# Import common libraries
from common.lib import data_processing, visualization, utils
```

### Example: Loading Data

```python
from common.lib import utils, data_processing

# Get dataset path for your notebook
dataset_path = utils.get_dataset_path('notebook_01')

# Load CSV data
data_file = dataset_path / 'your_data.csv'
df = data_processing.load_csv_data(data_file)
```

### Example: Visualization

```python
from common.lib import visualization

# Plot distribution
visualization.plot_distribution(df['column_name'], title='My Distribution')

# Plot correlation matrix
visualization.plot_correlation_matrix(df, title='Feature Correlations')
```

## 📦 Common Libraries

### data_processing.py
- `load_csv_data()`: Load CSV files
- `clean_missing_values()`: Handle missing values
- `normalize_column()`: Normalize data
- `get_basic_stats()`: Get statistical summaries

### visualization.py
- `plot_distribution()`: Histogram plots
- `plot_correlation_matrix()`: Correlation heatmaps
- `plot_scatter()`: Scatter plots
- `plot_time_series()`: Time series plots

### utils.py
- `get_project_root()`: Get project root path
- `get_dataset_path()`: Get notebook's dataset path
- `load_config()`: Load configuration
- `save_config()`: Save configuration

## ➕ Adding New Notebooks

To add a new notebook to the project:

1. Create a new folder in the `notebooks/` directory:
```bash
mkdir -p notebooks/notebook_04/dataset
```

2. Create your Jupyter notebook:
```bash
cd notebooks/notebook_04
jupyter notebook
# Create a new notebook and save it as notebook_04.ipynb
```

3. Add a README.md to document your notebook

4. Place your datasets in the `dataset/` folder

## 🔧 Configuration

Edit `common/config/config.json` to customize project-wide settings:

```json
{
  "project_name": "Notebooks Project",
  "common_settings": {
    "random_seed": 42,
    "plot_style": "whitegrid",
    "figure_dpi": 100
  }
}
```

## 📊 Example Notebooks

### Notebook 01: Example Data Analysis
Demonstrates the basic usage of common libraries with sample data, including:
- Data loading and cleaning
- Statistical analysis
- Visualization examples

### Notebook 02: Advanced Analysis
Template for advanced analysis techniques

### Notebook 03: Custom Analysis
Blank template for your custom analysis

## 🤝 Contributing

1. Create a new branch for your notebook or feature
2. Add your analysis in a new notebook folder
3. Document your work in the notebook's README
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 💡 Tips

- Keep datasets in their respective `dataset/` folders
- Use the common libraries to avoid code duplication
- Document your notebooks with markdown cells
- Update configuration in `common/config/config.json` for project-wide settings
- Add new shared functions to `common/lib/` when you have reusable code

## 🐛 Troubleshooting

### Import errors
Make sure the project root is added to your Python path:
```python
import sys
from pathlib import Path
project_root = Path().absolute().parent.parent
sys.path.insert(0, str(project_root))
```

### Module not found
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## 📞 Contact

For questions or suggestions, please open an issue on GitHub.