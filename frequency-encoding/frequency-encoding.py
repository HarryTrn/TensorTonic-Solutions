"""
 *     author:  _Shikimori_
 *     created: 02.11.2026 12:09:09
"""
def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    # Write code here
    freq = {value: values.count(value) / len(values) for value in set(values)}
    return [freq[value] for value in values]
    