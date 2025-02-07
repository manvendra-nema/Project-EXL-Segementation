import json

class JSONComparator:
    def __init__(self):
        self.summary = {
            "correct": {},
            "edited": {},
            "added": {},
            "deleted": {},
            "not_available": {}
        }

    def is_empty(self, val):
        """
        Returns True if val is considered empty (only for strings or lists).
        """
        return isinstance(val, (str, list)) and len(val) == 0

    def update_summary(self, change_type, path):
        """
        Updates the summary for a given change type using the full key path.
        The full path is built by joining all keys in the path with " -> ".
        """
        full_path = " -> ".join(path) if path else "root"
        self.summary[change_type].setdefault(full_path, 0)
        self.summary[change_type][full_path] += 1

    def compare_and_update(self, val1, val2, path):
        """
        Compares two primitive values (or strings/lists) and updates the summary:
          - If they are identical and non‑empty → "correct"
          - If val1 is empty and val2 is non‑empty → "added"
          - If val1 is non‑empty and val2 is empty → "deleted"
          - Otherwise (non‑empty to non‑empty but different) → "edited"
        """
        if val1 == val2:
            if not (isinstance(val1, (str, list)) and self.is_empty(val1)):
                self.update_summary("correct", path)
        else:
            if isinstance(val1, (str, list)) and self.is_empty(val1) and \
               not (isinstance(val2, (str, list)) and self.is_empty(val2)):
                self.update_summary("added", path)
            elif not (isinstance(val1, (str, list)) and self.is_empty(val1)) and \
                 (isinstance(val2, (str, list)) and self.is_empty(val2)):
                self.update_summary("deleted", path)
            else:
                self.update_summary("edited", path)

    def compare_lists(self, list1, list2, current_path):
        """
        Compares two lists element‑by‑element.
          - If both lists are empty, marks them as "not_available".
          - Otherwise, compares common indices and then marks extra items as added or deleted.
        """
        # If both lists are empty, mark as not_available.
        if self.is_empty(list1) and self.is_empty(list2):
            self.update_summary("not_available", current_path)
            return

        min_len = min(len(list1), len(list2))
        # Compare common indices.
        for i in range(min_len):
            item_path = current_path + [f"[{i}]"]
            item1 = list1[i]
            item2 = list2[i]
            if isinstance(item1, dict) and isinstance(item2, dict):
                self.compare(item1, item2, item_path)
            elif isinstance(item1, list) and isinstance(item2, list):
                # Recurse for nested lists.
                self.compare_lists(item1, item2, item_path)
            else:
                self.compare_and_update(item1, item2, item_path)
        # Mark extra items in list1 as deleted.
        for i in range(min_len, len(list1)):
            item_path = current_path + [f"[{i}]"]
            self.update_summary("deleted", item_path)
        # Mark extra items in list2 as added.
        for i in range(min_len, len(list2)):
            item_path = current_path + [f"[{i}]"]
            self.update_summary("added", item_path)

    def compare(self, json1, json2, level_path=None):
        """
        Recursively compares two JSON objects (dictionaries) and updates the summary.
        The full key path is maintained in level_path.
        """
        if level_path is None:
            level_path = []

        # Get all keys present in either JSON.
        all_keys = set(json1.keys()).union(set(json2.keys()))
        for key in all_keys:
            current_path = level_path + [key]
            in_json1 = key in json1
            in_json2 = key in json2

            if in_json1 and in_json2:
                val1 = json1[key]
                val2 = json2[key]

                # If both values are empty (for strings or lists), mark as not_available.
                if (isinstance(val1, (str, list)) and self.is_empty(val1)) and \
                   (isinstance(val2, (str, list)) and self.is_empty(val2)):
                    self.update_summary("not_available", current_path)
                    continue

                # If both values are dictionaries, compare recursively.
                if isinstance(val1, dict) and isinstance(val2, dict):
                    self.compare(val1, val2, current_path)
                # If both values are lists, use the compare_lists helper.
                elif isinstance(val1, list) and isinstance(val2, list):
                    self.compare_lists(val1, val2, current_path)
                else:
                    self.compare_and_update(val1, val2, current_path)
            else:
                # Key exists only in one of the JSON objects.
                if in_json1:
                    self.update_summary("deleted", current_path)
                else:
                    self.update_summary("added", current_path)
        return self.summary

    def get_summary(self):
        return self.summary
