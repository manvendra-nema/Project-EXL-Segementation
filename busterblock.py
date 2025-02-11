import re
from collections import defaultdict

def usecase_adaptor( data, delimiter):
    """
    Adapts the given data by cleaning and reformatting the keys based on the specified delimiter.
    If two cleaned keys are the same, their values are summed instead of creating duplicates.
    """

    def clean_key(key):
        index_removed = re.sub(r" -> \[\d+\]", "", key)
        common_substring_removed = re.sub("modules -> output -> referral -> ", "", index_removed)
        return delimiter.join(common_substring_removed.split(" -> "))

    cleaned_data = {}

    for category, entries in data.items():
        merged_entries = defaultdict(int)  # Store merged values

        for k, v in entries.items():
            new_key = clean_key(k)
            merged_entries[new_key] += v  # Increase count instead of creating duplicate keys

        cleaned_data[category] = dict(merged_entries)  # Convert back to a normal dictionary

    return cleaned_data
