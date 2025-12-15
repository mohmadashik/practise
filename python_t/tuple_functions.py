"""
MODULE: tuple_notes
Purpose: Inbuilt tuple operations with consistent docstring structure:
topic, function syntax, usage (this is CODE), real life usecases, pros, cons.
"""


# ------------------------------------------------------
def demo_len():
    """
    TOPIC:
        len(tuple)

    FUNCTION SYNTAX:
        len(sequence)

    USAGE:
        t = (1, 2, 3)
        n = len(t)

    REAL LIFE USECASES:
        - Validate number of fixed fields (e.g., coordinates, CSV columns).
        - Quick size checks before processing packets/records.

    PROS:
        - O(1), trivial and fast.
        - Works on all sequences.

    CONS:
        - None significant.
    """
    return len((1, 2, 3))


# ------------------------------------------------------
def demo_tuple_constructor():
    """
    TOPIC:
        tuple(iterable) — constructor

    FUNCTION SYNTAX:
        tuple(iterable)

    USAGE:
        a = [1, 2, 3]
        t = tuple(a)
        t_empty = tuple()

    REAL LIFE USECASES:
        - Freezing a list of configuration values to prevent modification.
        - Returning lightweight immutable records from functions.

    PROS:
        - Creates an immutable, hashable sequence.
        - Cheap and idiomatic.

    CONS:
        - Immutable → cannot append/pop (must recreate).
    """
    a = [1, 2, 3]
    return tuple(a), tuple()


# ------------------------------------------------------
def demo_immutability_note():
    """
    TOPIC:
        Tuple immutability (concept)

    FUNCTION SYNTAX:
        (immutable_tuple[index] = value)  # not allowed

    USAGE:
        t = (1, 2, 3)
        # attempting t[0] = 10 will raise TypeError

    REAL LIFE USECASES:
        - Use tuples for fixed schema rows (e.g., database result rows).
        - Use as dict keys when composite key required.

    PROS:
        - Safer: prevents accidental mutation.
        - Hashable if all elements are hashable.

    CONS:
        - To modify you must create a new tuple (costly for large tuples).
    """
    t = (1, 2, 3)
    try:
        # demonstrate immutability behavior safely
        t[0] = 10
    except TypeError as e:
        return ("TypeError", str(e))
    return ("unexpected", t)


# ------------------------------------------------------
def demo_count():
    """
    TOPIC:
        tuple.count(value)

    FUNCTION SYNTAX:
        tuple.count(x)

    USAGE:
        t = (1, 2, 2, 3)
        c = t.count(2)

    REAL LIFE USECASES:
        - Counting occurrences in small fixed records.
        - Quick validation of flags in fixed-length tuples.

    PROS:
        - Simple API, O(n).

    CONS:
        - Scans whole tuple → O(n).
        - For large datasets use collections.Counter on lists.
    """
    return (1, 2, 2, 3).count(2)


# ------------------------------------------------------
def demo_index():
    """
    TOPIC:
        tuple.index(value)

    FUNCTION SYNTAX:
        tuple.index(x)

    USAGE:
        t = ('a', 'b', 'c')
        i = t.index('b')

    REAL LIFE USECASES:
        - Locate position of a field in fixed schema tuples.
        - Small lookups in configuration tuples.

    PROS:
        - Readable and direct.

    CONS:
        - O(n) scan.
        - Raises ValueError if not found.
    """
    t = ('a', 'b', 'c')
    return t.index('b')


# ------------------------------------------------------
def demo_unpacking():
    """
    TOPIC:
        tuple unpacking / starred unpack

    FUNCTION SYNTAX:
        a, b = tuple_val
        a, *rest, z = tuple_val

    USAGE:
        t = (10, 20, 30)
        a, b, c = t
        head, *tail = (1, 2, 3, 4)

    REAL LIFE USECASES:
        - Destructure returned fixed-size records (lat, lon).
        - Read CSV rows into named variables.
        - Grab prefix/suffix with starred unpacking.

    PROS:
        - Very concise and Pythonic.
        - Useful for positional structured data.

    CONS:
        - ValueError if sizes mismatch (unless using starred).
    """
    t = (10, 20, 30)
    a, b, c = t
    head, *tail = (1, 2, 3, 4)
    return (a, b, c), head, tail


# ------------------------------------------------------
def demo_slicing():
    """
    TOPIC:
        tuple slicing

    FUNCTION SYNTAX:
        tuple[start:end:step]

    USAGE:
        t = (0, 1, 2, 3, 4)
        part = t[1:4]
        rev = t[::-1]

    REAL LIFE USECASES:
        - Windowing fixed time series.
        - Splitting fixed-size packets or headers.

    PROS:
        - Non-destructive → returns new tuple (original preserved).
        - Expressive.

    CONS:
        - Slicing creates a new tuple → memory cost for large slices.
    """
    t = (0, 1, 2, 3, 4)
    return t[1:4], t[::-1]


# ------------------------------------------------------
def demo_concat_repeat():
    """
    TOPIC:
        tuple concatenation and repetition

    FUNCTION SYNTAX:
        t1 + t2
        t * n

    USAGE:
        a = (1, 2)
        b = (3,)
        c = a + b        # (1, 2, 3)
        d = a * 3        # (1,2,1,2,1,2)

    REAL LIFE USECASES:
        - Build composite keys or fixed headers.
        - Repeat patterns in test data generation.

    PROS:
        - Simple operators, readable.

    CONS:
        - Both create new tuples → costs proportional to size.
    """
    a = (1, 2)
    b = (3,)
    c = a + b
    d = a * 3
    return c, d


# ------------------------------------------------------
def demo_membership():
    """
    TOPIC:
        membership: value in tuple / value not in tuple

    FUNCTION SYNTAX:
        x in tuple
        x not in tuple

    USAGE:
        t = (1, 2, 3)
        found = 2 in t

    REAL LIFE USECASES:
        - Check allowed fixed options (enum-like lists).
        - Validate function args against fixed set of tokens.

    PROS:
        - Very readable and simple.

    CONS:
        - O(n) lookup. For frequent membership tests use set.
    """
    return 2 in (1, 2, 3)


# ------------------------------------------------------
def demo_aggregates():
    """
    TOPIC:
        max(), min(), sum() on tuples

    FUNCTION SYNTAX:
        max(tuple)
        min(tuple)
        sum(tuple)

    USAGE:
        t = (5, 1, 9)
        return max(t), min(t), sum(t)

    REAL LIFE USECASES:
        - Simple analytics on small numeric tuples.
        - Quick checks for thresholds.

    PROS:
        - Built-in, optimized functions.

    CONS:
        - Requires elements to be comparable / numeric.
    """
    t = (5, 1, 9)
    return max(t), min(t), sum(t)


# ------------------------------------------------------
def demo_to_list_and_back():
    """
    TOPIC:
        convert between tuple and list

    FUNCTION SYNTAX:
        list(tuple)
        tuple(list)

    USAGE:
        t = (1, 2, 3)
        lst = list(t)
        t2 = tuple(lst)

    REAL LIFE USECASES:
        - Convert to list to mutate, then back to tuple to freeze.
        - Interop with APIs expecting lists vs tuples.

    PROS:
        - Flexible conversion when mutation required.

    CONS:
        - Copying costs (O(n)).
    """
    t = (1, 2, 3)
    lst = list(t)
    t2 = tuple(lst)
    return lst, t2


# ------------------------------------------------------
def demo_namedtuple_short():
    """
    TOPIC:
        collections.namedtuple — tuple-like with named fields (std lib helper)

    FUNCTION SYNTAX:
        from collections import namedtuple
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(1, 2)

    USAGE:
        from collections import namedtuple
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(10, 20)
        # access with p.x and p[0]

    REAL LIFE USECASES:
        - Return lightweight records with field names (e.g., DB row with columns).
        - Cleaner code than index-based tuple access in small domains.

    PROS:
        - Readable named fields, still tuple-behavior (immutable & indexable).
        - Memory-efficient compared to full classes.

    CONS:
        - Not as feature-rich as dataclasses.
        - Slightly verbose to declare.
    """
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    return p, p.x, p[0]
