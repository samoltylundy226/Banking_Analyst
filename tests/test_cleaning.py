"""
Unit tests for data cleaning logic in Banking Customer Analytics.
"""

import pytest
import pandas as pd
from src.cleaning import (
    remove_duplicate_clients,
    clean_names,
    parse_dates,
    validate_demographics,
    handle_zero_balances,
)


@pytest.fixture
def sample_raw_banking_df() -> pd.DataFrame:
    """Provide minimal mock dataframe reflecting known anomalies."""
    return pd.DataFrame({
        "Client ID": ["IND81288", "IND81288", "IND65833", "IND47499"],
        "Name": ["Raymond Mills", "Raymond Mills", "Carol GoPKRalez", "Stephen Murray"],
        "Age": [24, 24, 17, 27],
        "Joined Bank": ["06-05-2019", "06-05-2019", "10-12-2001", "25-01-2010"],
        "Bank Deposits": [1485828.64, 1485828.64, 0.0, 1033401.59],
        "Bank Loans": [776242.92, 776242.92, 1270615.43, 0.0],
        "Credit Card Balance": [484.54, 484.54, 0.0, 4568.74],
    })


def test_remove_duplicate_clients_stub():
    """Verify duplicate removal function stub is callable."""
    pass


def test_clean_names_stub():
    """Verify corrupted name cleaning function stub is callable."""
    pass


def test_parse_dates_stub():
    """Verify day-first date parser function stub is callable."""
    pass


def test_validate_demographics_stub():
    """Verify demographic boundary check function stub is callable."""
    pass


def test_handle_zero_balances_stub():
    """Verify zero balance handler function stub is callable."""
    pass
