"""
MODULE: set_notes
Purpose: Inbuilt set operations with consistent docstring structure:
topic, function syntax, usage (this is CODE), real life usecases, pros, cons.
"""


# ------------------------------------------------------
def demo_constructor_literal():
    """
    TOPIC:
        set() constructor and {} literal

    FUNCTION SYNTAX:
        set(iterable)
        {items}

    USAGE:
        s1 = set([1, 2, 3])
        s2 = {1, 2, 3}

    REAL LIFE USECASES:
        - Removing duplicates from collections.
        - Fast membership checks.
        - Turning lists into unique user IDs or values.

    PROS:
        - O(1) average membership.
        - Very fast deduplication.

    CONS:
        - Unordered → no indexing.
        - Cannot contain unhashable types (list/dict).
    """
    return set([1, 2, 3]), {1, 2, 3}


# ------------------------------------------------------
def demo_add():
    """
    TOPIC:
        set.add(value)

    FUNCTION SYNTAX:
        s.add(x)

    USAGE:
        s = {1, 2}
        s.add(3)

    REAL LIFE USECASES:
        - Add unique visitors/users.
        - Maintain unique tags in logs.
        - Build unique sets of keys from stream events.

    PROS:
        - O(1) average insert.
    CONS:
        - Ignores duplicates silently.
    """
    s = {1, 2}
    s.add(3)
    return s


# ------------------------------------------------------
def demo_remove():
    """
    TOPIC:
        set.remove(value)

    FUNCTION SYNTAX:
        s.remove(x)

    USAGE:
        s = {1, 2, 3}
        s.remove(2)

    REAL LIFE USECASES:
        - Removing expired IDs or tokens.
        - Removing tracked users from active sets.

    PROS:
        - Clear intent.

    CONS:
        - Raises KeyError if value not present.
    """
    s = {1, 2, 3}
    s.remove(2)
    return s


# ------------------------------------------------------
def demo_discard():
    """
    TOPIC:
        set.discard(value)

    FUNCTION SYNTAX:
        s.discard(x)

    USAGE:
        s = {1, 2, 3}
        s.discard(5)

    REAL LIFE USECASES:
        - Safely remove IDs that may or may not exist.
        - Good for event-based cleanup.

    PROS:
        - No error if item missing.

    CONS:
        - Silently ignores missing keys (might hide bugs).
    """
    s = {1, 2, 3}
    s.discard(5)
    return s


# ------------------------------------------------------
def demo_pop():
    """
    TOPIC:
        set.pop()

    FUNCTION SYNTAX:
        s.pop()

    USAGE:
        s = {10, 20, 30}
        x = s.pop()

    REAL LIFE USECASES:
        - Randomly consume elements if order doesn't matter.
        - Reduce memory by gradually draining sets.

    PROS:
        - Handy for iteratively consuming a set.

    CONS:
        - Removes arbitrary element → not predictable.
    """
    s = {10, 20, 30}
    removed = s.pop()
    return removed, s


# ------------------------------------------------------
def demo_clear():
    """
    TOPIC:
        set.clear()

    FUNCTION SYNTAX:
        s.clear()

    USAGE:
        s = {1, 2, 3}
        s.clear()

    REAL LIFE USECASES:
        - Resetting unique caches.
        - Dropping all tracked IDs.

    PROS:
        - O(1) wipe.
    CONS:
        - Shared references also see empty set.
    """
    s = {1, 2, 3}
    s.clear()
    return s


# ------------------------------------------------------
def demo_union():
    """
    TOPIC:
        set union

    FUNCTION SYNTAX:
        s1 | s2
        s1.union(s2)

    USAGE:
        a = {1, 2}
        b = {3, 4}
        c = a | b

    REAL LIFE USECASES:
        - Combine unique user IDs from multiple sources.
        - Merge tag sets.
        - Aggregate feature sets.

    PROS:
        - Fast, clean syntax.
    CONS:
        - Creates a new set (unless using update()).
    """
    a = {1, 2}
    b = {3, 4}
    return a | b


# ------------------------------------------------------
def demo_intersection():
    """
    TOPIC:
        set intersection

    FUNCTION SYNTAX:
        s1 & s2
        s1.intersection(s2)

    USAGE:
        a = {1, 2, 3}
        b = {2, 3, 4}
        c = a & b  # {2,3}

    REAL LIFE USECASES:
        - Find common users between systems.
        - Determine overlapping permissions.
        - Compute shared tags/categories.

    PROS:
        - Very fast set math.
    CONS:
        - Cost proportional to smaller set.
    """
    a = {1, 2, 3}
    b = {2, 3, 4}
    return a & b


# ------------------------------------------------------
def demo_difference():
    """
    TOPIC:
        set difference

    FUNCTION SYNTAX:
        s1 - s2
        s1.difference(s2)

    USAGE:
        a = {1,2,3}
        b = {2}
        c = a - b  # {1,3}

    REAL LIFE USECASES:
        - Find users who unsubscribed.
        - Detect missing permissions.
        - Identify removed items.

    PROS:
        - Very expressive.
    CONS:
        - Creates new set unless using difference_update().
    """
    a = {1, 2, 3}
    b = {2}
    return a - b


# ------------------------------------------------------
def demo_symmetric_difference():
    """
    TOPIC:
        symmetric difference (elements in one OR the other, not both)

    FUNCTION SYNTAX:
        s1 ^ s2
        s1.symmetric_difference(s2)

    USAGE:
        a = {1,2,3}
        b = {3,4}
        c = a ^ b  # {1,2,4}

    REAL LIFE USECASES:
        - Compare two states and find changed items.
        - Detect mismatched IDs.

    PROS:
        - Great for diff operations.
    CONS:
        - Creates new set.
    """
    a = {1, 2, 3}
    b = {3, 4}
    return a ^ b


# ------------------------------------------------------
def demo_update_operations():
    """
    TOPIC:
        in-place update operations (|=, &=, -=, ^=)

    FUNCTION SYNTAX:
        s |= other
        s &= other
        s -= other
        s ^= other

    USAGE:
        s = {1,2}
        s |= {3}   # union update

    REAL LIFE USECASES:
        - Maintain active sets efficiently.
        - Reduce memory by modifying in-place.
        - Streaming set operations.

    PROS:
        - Avoids creating new sets.
    CONS:
        - Destructive → original data lost.
    """
    s = {1, 2}
    s |= {3}
    return s


# ------------------------------------------------------
def demo_membership():
    """
    TOPIC:
        membership: x in set

    FUNCTION SYNTAX:
        x in s
        x not in s

    USAGE:
        s = {10,20,30}
        check = 20 in s

    REAL LIFE USECASES:
        - Check if user visited already.
        - Check if token exists in blacklist.
        - Fast validation lookups.

    PROS:
        - O(1) average lookup — best structure for membership.
    CONS:
        - Unordered — not useful for positional logic.
    """
    return 20 in {10, 20, 30}


# ------------------------------------------------------
def demo_frozenset():
    """
    TOPIC:
        frozenset (immutable set)

    FUNCTION SYNTAX:
        frozenset(iterable)

    USAGE:
        fs = frozenset([1,2,3])

    REAL LIFE USECASES:
        - Use as dict keys (hashable set).
        - Safe permission sets that must not change.
        - Cache keys for function memoization.

    PROS:
        - Immutable, hashable.
        - Same operations as sets except mutation.

    CONS:
        - Cannot add/remove items.
    """
    return frozenset([1, 2, 3])
