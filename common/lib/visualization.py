"""
Common visualization utilities for all notebooks.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, Tuple


# Set default style
sns.set_style("whitegrid")


def plot_distribution(data: pd.Series, title: str = "Distribution", 
                     figsize: Tuple[int, int] = (10, 6), bins: int = 30) -> None:
    """
    Plot distribution of a data series.
    
    Args:
        data: Data to plot
        title: Plot title
        figsize: Figure size (width, height)
        bins: Number of bins for histogram
    """
    plt.figure(figsize=figsize)
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df: pd.DataFrame, title: str = "Correlation Matrix",
                            figsize: Tuple[int, int] = (12, 10)) -> None:
    """
    Plot correlation matrix heatmap.
    
    Args:
        df: Input dataframe
        title: Plot title
        figsize: Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    correlation = df.corr()
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_scatter(x: pd.Series, y: pd.Series, title: str = "Scatter Plot",
                xlabel: str = "X", ylabel: str = "Y", 
                figsize: Tuple[int, int] = (10, 6)) -> None:
    """
    Plot scatter plot of two series.
    
    Args:
        x: X-axis data
        y: Y-axis data
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        figsize: Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    plt.scatter(x, y, alpha=0.6)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_time_series(df: pd.DataFrame, date_column: str, value_column: str,
                     title: str = "Time Series", figsize: Tuple[int, int] = (14, 6)) -> None:
    """
    Plot time series data.
    
    Args:
        df: Input dataframe
        date_column: Name of the date column
        value_column: Name of the value column
        title: Plot title
        figsize: Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    plt.plot(df[date_column], df[value_column], linewidth=2)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(value_column)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
