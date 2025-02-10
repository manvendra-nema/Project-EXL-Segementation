# --------------------- Test Cases ---------------------

# Test for "correct" operation
def test_correct_operation():
    comparator = JSONComparator()
    json1 = {"a": {"b": "value"}}
    json2 = {"a": {"b": "value"}}
    summary = comparator.compare(json1, json2)
    expected = {
        "correct": {"a -> b": 1},
        "edited": {},
        "added": {},
        "deleted": {},
        "not_available": {}
    }
    assert summary == expected

# Test for "edited" operation (non-empty to non-empty change)
def test_edited_operation():
    comparator = JSONComparator()
    json1 = {"a": {"b": "old"}}
    json2 = {"a": {"b": "new"}}
    summary = comparator.compare(json1, json2)
    expected = {
        "correct": {},
        "edited": {"a -> b": 1},
        "added": {},
        "deleted": {},
        "not_available": {}
    }
    assert summary == expected

# Test for "added" operation (empty to non-empty)
def test_added_operation():
    comparator = JSONComparator()
    json1 = {"a": {"b": ""}}
    json2 = {"a": {"b": "value"}}
    summary = comparator.compare(json1, json2)
    expected = {
        "correct": {},
        "edited": {},
        "added": {"a -> b": 1},
        "deleted": {},
        "not_available": {}
    }
    assert summary == expected

# Test for "deleted" operation (non-empty to empty)
def test_deleted_operation():
    comparator = JSONComparator()
    json1 = {"a": {"b": "value"}}
    json2 = {"a": {"b": ""}}
    summary = comparator.compare(json1, json2)
    expected = {
        "correct": {},
        "edited": {},
        "added": {},
        "deleted": {"a -> b": 1},
        "not_available": {}
    }
    assert summary == expected

# Test for "not_available" operation (both empty)
def test_not_available_operation():
    comparator = JSONComparator()
    json1 = {"a": {"b": ""}}
    json2 = {"a": {"b": ""}}
    summary = comparator.compare(json1, json2)
    expected = {
        "correct": {},
        "edited": {},
        "added": {},
        "deleted": {},
        "not_available": {"a -> b": 1}
    }
    assert summary == expected

# ------------------ Very Complicated Nested Structures ------------------

def test_complicated_structure_1():
    comparator = JSONComparator()
    json1 = {
        "user": {
            "id": 1,
            "profile": {
                "name": "Alice",
                "emails": ["alice@example.com", ""],
                "address": {"city": "Wonderland", "zip": "12345"},
                "preferences": {"notifications": True, "languages": ["English", "Spanish"]}
            },
            "activities": [
                {"type": "login", "time": "2025-01-01T09:00:00Z"},
                {"type": "purchase", "amount": 50}
            ]
        },
        "metadata": {"tags": [], "version": 1}
    }
    json2 = {
        "user": {
            "id": 1,
            "profile": {
                "name": "Alice",
                "emails": ["alice@example.com", "alice@work.com"],  # second email: added (empty->non-empty)
                "address": {"city": "Wonderland", "zip": "12345"},
                "preferences": {"notifications": False, "languages": ["English", "French"]}  # edited changes
            },
            "activities": [
                {"type": "login", "time": "2025-01-01T09:00:00Z"},
                {"type": "purchase", "amount": 50},
                {"type": "logout", "time": "2025-01-01T09:05:00Z"}  # extra: added
            ]
        },
        "metadata": {"tags": [], "version": 2}  # version edited
    }
    summary = comparator.compare(json1, json2)
    # Assert some expected changes:
    assert summary["added"].get("user -> profile -> emails -> [1]", 0) == 1
    assert summary["edited"].get("user -> profile -> preferences -> notifications", 0) == 1
    assert summary["edited"].get("user -> profile -> preferences -> languages -> [1]", 0) == 1
    assert summary["added"].get("user -> activities -> [2]", 0) == 1
    assert summary["edited"].get("metadata -> version", 0) == 1

def test_complicated_structure_2():
    comparator = JSONComparator()
    json1 = {
        "data": {
            "items": [
                {"id": 1, "values": [[1,2], [3,4]]},
                {"id": 2, "values": [[5,6], []]}
            ],
            "config": {"threshold": 10, "modes": ["auto", "manual"]}
        }
    }
    json2 = {
        "data": {
            "items": [
                {"id": 1, "values": [[1,2], [3,5,7]]},   # nested list difference in second sub-list
                {"id": 2, "values": [[5,6], []]},
                {"id": 3, "values": [[8,9]]}              # extra item: added
            ],
            "config": {"threshold": 12, "modes": ["auto", "manual"]}  # threshold edited
        }
    }
    summary = comparator.compare(json1, json2)
    # In items[0] second nested list:
    assert summary["correct"].get("data -> items -> [0] -> values -> [1] -> [0]", 0) == 1  # 3 vs 3 is correct
    assert summary["edited"].get("data -> items -> [0] -> values -> [1] -> [1]", 0) == 1   # 4 vs 5 is edited
    assert summary["added"].get("data -> items -> [0] -> values -> [1] -> [2]", 0) == 1    # extra element 7 added
    assert summary["edited"].get("data -> config -> threshold", 0) == 1
    assert summary["added"].get("data -> items -> [2]", 0) == 1  # extra item for id 3

def test_complicated_structure_3():
    comparator = JSONComparator()
    json1 = {
        "system": {
            "modules": [
                {"name": "mod1", "settings": {"enabled": True, "params": [10, 20]}},
                {"name": "mod2", "settings": {"enabled": False, "params": [30]}}
            ],
            "logs": [
                {"date": "2025-01-01", "entries": ["start", "init"]},
                {"date": "2025-01-02", "entries": []}
            ]
        },
        "version": "1.0.0"
    }
    json2 = {
        "system": {
            "modules": [
                {"name": "mod1", "settings": {"enabled": True, "params": [10, 25]}},  # 20 → 25: edited
                {"name": "mod2", "settings": {"enabled": True, "params": [30]}},       # False → True: edited
                {"name": "mod3", "settings": {"enabled": True, "params": []}}            # extra: added
            ],
            "logs": [
                {"date": "2025-01-01", "entries": ["start", "init", "complete"]},      # extra entry: added
                {"date": "2025-01-02", "entries": []}                                   # both empty: not_available
            ]
        },
        "version": "1.1.0"   # edited
    }
    summary = comparator.compare(json1, json2)
    assert summary["edited"].get("system -> modules -> [0] -> settings -> params -> [1]", 0) == 1
    assert summary["edited"].get("system -> modules -> [1] -> settings -> enabled", 0) == 1
    assert summary["added"].get("system -> modules -> [2]", 0) == 1
    assert summary["added"].get("system -> logs -> [0] -> entries -> [2]", 0) == 1
    assert summary["not_available"].get("system -> logs -> [1] -> entries", 0) == 1
    assert summary["edited"].get("version", 0) == 1

# --------------------- Pytest Main Entry ---------------------
if __name__ == "__main__":
    pytest.main([__file__])
