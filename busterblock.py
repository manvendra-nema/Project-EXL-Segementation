import re
from collections import defaultdict

def usecase_adaptor(self, data, delimiter):
    """
    Adapts the given data by cleaning and reformatting the keys based on the specified delimiter.

    The input data where each key is a category and the value is a dictionary of entries.
    The delimiter to use for joining the cleaned key parts.
    """
    def clean_key(key):
        index_removed = re.sub(r" -> \[\d+\]", "", key)
        common_substring_removed = re.sub("modules -> output -> referral -> ", "", index_removed)
        return delimiter.join(common_substring_removed.split(" -> "))

    cleaned_data = {}

    for category, entries in data.items():
        key_count = defaultdict(int)  # Track occurrences of each cleaned key
        cleaned_entries = {}

        for k, v in entries.items():
            new_key = clean_key(k)
            key_count[new_key] += 1

            # If key already exists, append a counter to differentiate
            if key_count[new_key] > 1:
                new_key = f"{new_key}_{key_count[new_key]}"

            cleaned_entries[new_key] = v

        cleaned_data[category] = cleaned_entries

    return cleaned_data
