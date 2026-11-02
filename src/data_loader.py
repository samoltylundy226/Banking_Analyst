"""
Data loading utilities for Banking Customer Analytics.

Provides functions to load raw, interim, and processed data assets.
"""

from pathlib import Path
from typing import Optional, Union
import pandas as pd


def load_raw(filepath: Optional[Union[Path, str]] = None) -> pd.DataFrame:
    """
    Load raw Banking.csv dataset with utf-8-sig encoding.

    Parameters
    ----------
    filepath : Path or str, optional
        Path to Banking.csv file. If None, defaults to data/raw/Banking.csv
        relative to the project root directory.

    Returns
    -------
    pd.DataFrame
        Raw customer dataframe loaded with utf-8-sig encoding.
    """
    if filepath is None:
        filepath = Path(__file__).resolve().parent.parent / "data" / "raw" / "Banking.csv"
    return pd.read_csv(filepath, encoding="utf-8-sig")


def load_interim(filepath: Optional[Union[Path, str]] = None) -> pd.DataFrame:
    """
    Load interim (partially cleaned) dataset.

    Parameters
    ----------
    filepath : Path or str, optional
        Path to interim CSV file.

    Returns
    -------
    pd.DataFrame
        Interim customer dataframe.
    """
    pass


def load_processed(filepath: Optional[Union[Path, str]] = None) -> pd.DataFrame:
    """
    Load final cleaned and validated dataset ready for analysis.

    Parameters
    ----------
    filepath : Path or str, optional
        Path to processed CSV file.

    Returns
    -------
    pd.DataFrame
        Processed customer analytics dataframe.
    """
    pass
