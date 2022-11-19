import datetime
import pandas as pd
import pytest
from extract_birth_year import get_birth_year

def test_get_birth_year():
    # Arrange
    expected_data = [['tom', 10, 2012], ['nick', 15, 2007], ['juli', 14, 2008]]
    df_expected_output = pd.DataFrame(expected_data, columns=['Name', 'Age','birth_year'])
    # Act
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    df_actual = pd.DataFrame(data, columns=['Name', 'Age'])
    df_actual_output = get_birth_year(df_actual)
    #Assert
    assert df_actual_output.equals(df_expected_output)

def test_get_birth_year_unclean_data():
    # Arrange
    year = datetime.date.today().year
    expected_data = [['tom', 0, year], ['nick', 15, 2007], ['juli', 14, 2008]]
    df_expected_output = pd.DataFrame(expected_data, columns=['Name', 'Age','birth_year'])
    # Act
    data = [['tom', True], ['nick', 15], ['juli', 14]]
    df_actual = pd.DataFrame(data, columns=['Name', 'Age'])
    df_actual_output = get_birth_year(df_actual)
    #Assert
    assert df_actual_output.equals(df_expected_output)

def test_get_birth_year_unsupported_excpetion():
    # Arrange & Act
    data = [['krish', 1], ['jack', 50], ['elon', 100]]
    df_input = pd.DataFrame(data, columns=['Name', 'Amount'])
    with pytest.raises(NotImplementedError) as exc_info:
        df_actual_output = get_birth_year(df_input)
    # Assert
    assert exc_info.type is NotImplementedError
    assert exc_info.value.args[0] == "unsupported dataframe"