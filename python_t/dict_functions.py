"""
MODULE: dict_notes
Purpose: Inbuilt dict operations with consistent docstring structure:
topic, function syntax, usage (this is CODE), real life usecases, pros, cons.
"""


# ------------------------------------------------------
def demo_len():
    """
    TOPIC:
        len(dict)

    FUNCTION SYNTAX:
        len(mapping)

    USAGE:
        d = {'a': 1, 'b': 2}
        n = len(d)

    REAL LIFE USECASES:
        - Quick count of keys (e.g., number of users in cache).
        - Validate required config entries exist.

    PROS:
        - O(1), trivial and fast.
    CONS:
        - None significant.
    """
    return len({'a': 1, 'b': 2})


# ------------------------------------------------------
def demo_constructor_literal():
    """
    TOPIC:
        dict(...) constructor and {} literal

    FUNCTION SYNTAX:
        dict(iterable_or_mapping)
        {}  # literal

    USAGE:
        d1 = dict(a=1, b=2)
        d2 = dict([('a', 1), ('b', 2)])
        d3 = {'a': 1, 'b': 2}

    REAL LIFE USECASES:
        - Build mappings from DB rows, JSON, or function args.
        - Literal for fixed config inline.

    PROS:
        - Flexible construction options.
        - Fast and idiomatic.
    CONS:
        - Using dict() on sequences requires correct pair structure.
    """
    d1 = dict(a=1, b=2)
    d2 = dict([('a', 1), ('b', 2)])
    d3 = {'a': 1, 'b': 2}
    return d1, d2, d3


# ------------------------------------------------------
def demo_get():
    """
    TOPIC:
        dict.get(key, default=None)

    FUNCTION SYNTAX:
        mapping.get(key[, default])

    USAGE:
        d = {'x': 10}
        a = d.get('x')       # 10
        b = d.get('y', 0)    # 0

    REAL LIFE USECASES:
        - Safe lookup for optional fields in payloads.
        - Read config with fallback defaults.

    PROS:
        - Avoids KeyError.
        - Simple default handling.

    CONS:
        - Default might mask missing-key bugs if used carelessly.
    """
    d = {'x': 10}
    return d.get('x'), d.get('y', 0)


# ------------------------------------------------------
def demo_setitem():
    """
    TOPIC:
        setting items (assignment)

    FUNCTION SYNTAX:
        mapping[key] = value

    USAGE:
        d = {}
        d['user'] = 'ashik'

    REAL LIFE USECASES:
        - Update cache entries.
        - Upsert config values.

    PROS:
        - Simple and explicit.
    CONS:
        - Overwrites silently if key exists (use caution).
    """
    d = {}
    d['user'] = 'ashik'
    return d


# ------------------------------------------------------
def demo_setdefault():
    """
    TOPIC:
        dict.setdefault(key, default=None)

    FUNCTION SYNTAX:
        mapping.setdefault(key[, default])

    USAGE:
        d = {}
        lst = d.setdefault('items', [])
        lst.append(1)
        # d -> {'items': [1]}

    REAL LIFE USECASES:
        - Grouping or accumulating values (e.g., bucketization).
        - Initialize nested structures safely.

    PROS:
        - Useful one-liner to ensure key exists.
    CONS:
        - Default object is created only if key absent; careful with mutable defaults.
        - Can silently create keys (side-effect).
    """
    d = {}
    lst = d.setdefault('items', [])
    lst.append(1)
    return d


# ------------------------------------------------------
def demo_update():
    """
    TOPIC:
        dict.update(other)  # merge in-place

    FUNCTION SYNTAX:
        mapping.update(mapping_or_iterable)

    USAGE:
        a = {'x': 1}
        b = {'y': 2}
        a.update(b)   # a -> {'x':1, 'y':2}

    REAL LIFE USECASES:
        - Merge config from multiple sources.
        - Apply patch/update to state caches.

    PROS:
        - In-place, fast, handles many input types.
    CONS:
        - Overwrites keys; can clobber unintentionally.
    """
    a = {'x': 1}
    b = {'y': 2}
    a.update(b)
    return a


# ------------------------------------------------------
def demo_keys_values_items():
    """
    TOPIC:
        dict.keys(), dict.values(), dict.items()

    FUNCTION SYNTAX:
        mapping.keys()
        mapping.values()
        mapping.items()

    USAGE:
        d = {'a': 1, 'b': 2}
        ks = list(d.keys())
        vs = list(d.values())
        its = list(d.items())

    REAL LIFE USECASES:
        - Iterate keys/values/pairs for serialization, logging, or transforms.
        - Build reverse maps or indexes.

    PROS:
        - Return dynamic view objects (reflect changes).
        - Efficient iteration without copying.
    CONS:
        - Views may be surprising if mapping mutates during iteration.
    """
    d = {'a': 1, 'b': 2}
    return list(d.keys()), list(d.values()), list(d.items())


# ------------------------------------------------------
def demo_pop():
    """
    TOPIC:
        dict.pop(key[, default])

    FUNCTION SYNTAX:
        mapping.pop(key[, default])

    USAGE:
        d = {'a': 1, 'b': 2}
        x = d.pop('a')      # 1
        y = d.pop('z', None)  # None (no KeyError)

    REAL LIFE USECASES:
        - Remove-and-process pattern (consume a task from dict).
        - Safe removals when key may be missing.

    PROS:
        - Returns removed value.
    CONS:
        - Raises KeyError if no default provided and key missing.
    """
    d = {'a': 1, 'b': 2}
    x = d.pop('a')
    y = d.pop('z', None)
    return x, y, d


# ------------------------------------------------------
def demo_popitem():
    """
    TOPIC:
        dict.popitem()

    FUNCTION SYNTAX:
        mapping.popitem()

    USAGE:
        d = {'a': 1, 'b': 2}
        key, val = d.popitem()  # removes last inserted pair (Python 3.7+)

    REAL LIFE USECASES:
        - LIFO-style consumption for small caches.
        - Drain a dict while processing items.

    PROS:
        - Fast removal of an arbitrary/last item.
    CONS:
        - Order-specific behavior depends on insertion order (recent behaviour).
    """
    d = {'a': 1, 'b': 2}
    item = d.popitem()
    return item, d


# ------------------------------------------------------
def demo_clear():
    """
    TOPIC:
        dict.clear()

    FUNCTION SYNTAX:
        mapping.clear()

    USAGE:
        d = {'a': 1}
        d.clear()  # {}

    REAL LIFE USECASES:
        - Reset caches or temporary mappings.
        - Reuse mapping object while wiping data.

    PROS:
        - Quick wipe, O(1) semantics.
    CONS:
        - Shared references to mapping will see cleared state.
    """
    d = {'a': 1}
    d.clear()
    return d


# ------------------------------------------------------
def demo_copy():
    """
    TOPIC:
        dict.copy()

    FUNCTION SYNTAX:
        mapping.copy()

    USAGE:
        d = {'a': {'x': 1}}
        shallow = d.copy()
        shallow['a']['x'] = 2  # original d['a']['x'] also changes

    REAL LIFE USECASES:
        - Snapshot mapping before modifications.
        - Pass a copy to a worker to avoid mutating original reference binding.

    PROS:
        - Fast, shallow copy for top-level keys.
    CONS:
        - Shallow: nested mutable values are shared (use deepcopy if needed).
    """
    import copy as _copy
    d = {'a': {'x': 1}}
    shallow = d.copy()
    # demonstrate shallow behavior
    shallow['a']['x'] = 2
    # reset to show original mutated
    d_reset = _copy.deepcopy({'a': {'x': 1}})
    return shallow, d, d_reset


# ------------------------------------------------------
def demo_fromkeys():
    """
    TOPIC:
        dict.fromkeys(iterable, value=None)

    FUNCTION SYNTAX:
        dict.fromkeys(keys[, value])

    USAGE:
        keys = ['a', 'b']
        d = dict.fromkeys(keys, 0)  # {'a':0, 'b':0}

    REAL LIFE USECASES:
        - Initialize default-valued maps (e.g., counts).
        - Create mapping skeletons from a set of keys.

    PROS:
        - Quick initialization.
    CONS:
        - Beware using mutable default as same object will be shared.
    """
    keys = ['a', 'b']
    d = dict.fromkeys(keys, 0)
    return d


# ------------------------------------------------------
def demo_membership():
    """
    TOPIC:
        membership in dict (key in dict) and 'in' on values/keys

    FUNCTION SYNTAX:
        key in mapping
        val in mapping.values()

    USAGE:
        d = {'a': 1}
        has_key = 'a' in d
        has_val = 1 in d.values()

    REAL LIFE USECASES:
        - Permission checks, existence checks for user ids.
        - Validate config keys present.

    PROS:
        - Key lookup is O(1).
    CONS:
        - Value membership is O(n) (avoid if expensive).
    """
    d = {'a': 1}
    return ('a' in d), (1 in d.values())


# ------------------------------------------------------
def demo_comprehension():
    """
    TOPIC:
        dict comprehension

    FUNCTION SYNTAX:
        {k_expr: v_expr for item in iterable if cond}

    USAGE:
        pairs = [('a', 1), ('b', 2)]
        d = {k: v for k, v in pairs}

    REAL LIFE USECASES:
        - Transform list-of-tuples into maps quickly.
        - Build lookup dictionaries from records.

    PROS:
        - Concise and expressive.
    CONS:
        - Can be dense / less readable if complex expressions used.
    """
    pairs = [('a', 1), ('b', 2)]
    d = {k: v for k, v in pairs}
    return d


# ------------------------------------------------------
def demo_merge_pipe():
    """
    TOPIC:
        dict merge operators (Python 3.9+): | and |=

    FUNCTION SYNTAX:
        merged = dict1 | dict2   # new dict
        dict1 |= dict2           # update in-place

    USAGE:
        a = {'x': 1}
        b = {'y': 2}
        c = a | b
        a |= b

    REAL LIFE USECASES:
        - Immutable-style merges when you want new mapping result.
        - Apply patches immutably in functional-style code.

    PROS:
        - Clear syntax for merge; | returns new dict.
    CONS:
        - Requires Python >=3.9 for | operator.
    """
    a = {'x': 1}
    b = {'y': 2}
    c = a | b
    a |= b
    return c, a

print(f'demo_merge_pipe: {demo_merge_pipe()}')


# ------------------------------------------------------
def demo_nested_access_safe():
    """
    TOPIC:
        safe nested access (get + dict.get chaining)

    FUNCTION SYNTAX:
        mapping.get('a', {}).get('b')

    USAGE:
        data = {'user': {'id': 1}}
        uid = data.get('user', {}).get('id')

    REAL LIFE USECASES:
        - Read nested JSON payloads safely without exceptions.
        - Defensive code for optional nested fields.

    PROS:
        - Avoids KeyError on intermediate missing keys.
    CONS:
        - Verbose for very deep nesting; consider libraries (pydash, jmespath).
    """
    data = {'user': {'id': 1}}
    uid = data.get('user', {}).get('id')
    missing = data.get('profile', {}).get('age')
    return uid, missing


# ------------------------------------------------------
def demo_json_conversion():
    """
    TOPIC:
        JSON serialization/deserialization (dict <-> JSON)

    FUNCTION SYNTAX:
        json.dumps(mapping)
        json.loads(json_string)

    USAGE:
        import json
        d = {'a': 1}
        s = json.dumps(d)
        d2 = json.loads(s)

    REAL LIFE USECASES:
        - Send/receive HTTP payloads.
        - Persist configuration or logs.

    PROS:
        - Standard library, interoperable.
    CONS:
        - JSON only supports basic types; custom objects require encoding.
    """
    import json
    d = {'a': 1}
    s = json.dumps(d)
    d2 = json.loads(s)
    return s, d2


# ------------------------------------------------------
def demo_defaultdict_counter_short():
    """
    TOPIC:
        collections.defaultdict and collections.Counter (helpers)

    FUNCTION SYNTAX:
        from collections import defaultdict, Counter

    USAGE:
        from collections import defaultdict, Counter
        dd = defaultdict(list)
        dd['k'].append(1)

        c = Counter(['a', 'b', 'a'])

    REAL LIFE USECASES:
        - defaultdict: grouping/accumulation without setdefault boilerplate.
        - Counter: frequency counts (logs, telemetry, tokens).

    PROS:
        - Less boilerplate, expressive.
    CONS:
        - defaultdict hides missing-key bugs if used without care.
    """
    from collections import defaultdict, Counter
    dd = defaultdict(list)
    dd['k'].append(1)
    c = Counter(['a', 'b', 'a'])
    return dict(dd), dict(c)
