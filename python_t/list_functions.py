"""
MODULE: list_notes
Purpose: Inbuilt list functions with consistent docstring structure:
topic, function syntax, usage (code), real life usecases, pros, cons.
"""


# ------------------------------------------------------
def demo_len():
    """
    TOPIC:
        len(list)

    FUNCTION SYNTAX:
        len(sequence)

    USAGE:
        items = [10, 20, 30]
        size = len(items)

    REAL LIFE USECASES:
        - Checking payload lengths in APIs.
        - Ensuring minimum data received before processing.
        - Validating list sizes in pagination.

    PROS:
        - O(1) time.
        - Universally used.

    CONS:
        - None, extremely reliable.
    """
    return len([10, 20, 30])


# ------------------------------------------------------
def demo_append():
    """
    TOPIC:
        list.append(x)

    FUNCTION SYNTAX:
        list.append(item)

    USAGE:
        nums = [1, 2]
        nums.append(3)

    REAL LIFE USECASES:
        - Adding new log entries.
        - Building result lists inside loops.
        - Collecting streaming data.

    PROS:
        - O(1) average.
        - Very common and intuitive.

    CONS:
        - Only one item at a time.
        - Mutates list (side effects if shared).
    """
    nums = [1, 2]
    nums.append(3)
    return nums


# ------------------------------------------------------
def demo_extend():
    """
    TOPIC:
        list.extend(iterable)

    FUNCTION SYNTAX:
        list.extend([items])

    USAGE:
        a = [1, 2]
        a.extend([3, 4, 5])

    REAL LIFE USECASES:
        - Appending batched API results.
        - Merging lists from multiple services.
        - Expanding datasets efficiently.

    PROS:
        - More efficient than multiple append().
        - Clean and readable.

    CONS:
        - Mutates list.
        - Beginners confuse it with append().
    """
    a = [1, 2]
    a.extend([3, 4, 5])
    return a


# ------------------------------------------------------
def demo_insert():
    """
    TOPIC:
        list.insert(index, value)

    FUNCTION SYNTAX:
        list.insert(i, x)

    USAGE:
        items = ['a', 'c']
        items.insert(1, 'b')

    REAL LIFE USECASES:
        - Maintaining sorted/ordered sequences.
        - UI ordered menus.
        - Priority-based inserts.

    PROS:
        - Precise control over placement.

    CONS:
        - O(n) operation (shifts elements).
        - Bad for large lists in loops.
    """
    x = ['a', 'c']
    x.insert(1, 'b')
    return x


# ------------------------------------------------------
def demo_remove():
    """
    TOPIC:
        list.remove(value)

    FUNCTION SYNTAX:
        list.remove(x)

    USAGE:
        a = [1, 2, 2, 3]
        a.remove(2)

    REAL LIFE USECASES:
        - Cleaning unwanted values in datasets.
        - Removing selected items in UI lists.
        - Preprocessing text or logs.

    PROS:
        - Easy to remove specific values.

    CONS:
        - Removes ONLY the first match.
        - ValueError if item not found.
        - O(n) cost.
    """
    a = [1, 2, 2, 3]
    a.remove(2)
    return a


# ------------------------------------------------------
def demo_pop():
    """
    TOPIC:
        list.pop([index])

    FUNCTION SYNTAX:
        list.pop() or list.pop(i)

    USAGE:
        items = ['a', 'b', 'c']
        last = items.pop()
        first = items.pop(0)

    REAL LIFE USECASES:
        - Stack operations (pop last).
        - Processing tasks & removing them.
        - Simple queue (pop(0)) though inefficient.

    PROS:
        - pop() is O(1).
        - Returns the removed element.

    CONS:
        - pop(0) is O(n).
        - Mutates list.
    """
    items = ['a', 'b', 'c']
    return items.pop(), items


# ------------------------------------------------------
def demo_clear():
    """
    TOPIC:
        list.clear()

    FUNCTION SYNTAX:
        list.clear()

    USAGE:
        x = [1, 2, 3]
        x.clear()

    REAL LIFE USECASES:
        - Resetting buffers.
        - Clearing temporary result lists.
        - Reusing list objects in loops.

    PROS:
        - O(1) clear operation.
        - Keeps the same list reference.

    CONS:
        - If referenced elsewhere → everything empties.
    """
    x = [1, 2, 3]
    x.clear()
    return x


# ------------------------------------------------------
def demo_index():
    """
    TOPIC:
        list.index(value)

    FUNCTION SYNTAX:
        list.index(x)

    USAGE:
        nums = [10, 20, 30]
        i = nums.index(20)

    REAL LIFE USECASES:
        - Finding item positions in menus.
        - Locating user IDs / keys in short lists.
        - Quick search scenarios.

    PROS:
        - Very readable.

    CONS:
        - O(n).
        - Throws error if not found.
    """
    nums = [10, 20, 30]
    return nums.index(20)


# ------------------------------------------------------
def demo_count():
    """
    TOPIC:
        list.count(value)

    FUNCTION SYNTAX:
        list.count(x)

    USAGE:
        data = [1, 2, 2, 3]
        c = data.count(2)

    REAL LIFE USECASES:
        - Counting small duplicates.
        - Basic analytics.
        - Data validation (e.g., check if only one flag exists).

    PROS:
        - Simple, readable.

    CONS:
        - O(n) scan.
        - For big data → use collections.Counter.
    """
    return [1, 2, 2, 3].count(2)


# ------------------------------------------------------
def demo_reverse():
    """
    TOPIC:
        list.reverse()

    FUNCTION SYNTAX:
        list.reverse()

    USAGE:
        items = [1, 2, 3]
        items.reverse()

    REAL LIFE USECASES:
        - Reversing logs or history.
        - Reversing algorithm outputs.
        - Backward traversal.

    PROS:
        - In-place, fast.

    CONS:
        - Mutates order permanently.
    """
    x = [1, 2, 3]
    x.reverse()
    return x


# ------------------------------------------------------
def demo_sort():
    """
    TOPIC:
        list.sort()

    FUNCTION SYNTAX:
        list.sort(key=None, reverse=False)

    USAGE:
        nums = [3,1,2]
        nums.sort()

    REAL LIFE USECASES:
        - Leaderboard sorting.
        - Sorting DB results.
        - Cleaning and organizing data.

    PROS:
        - Extremely optimized (Timsort).
        - Supports custom keys.

    CONS:
        - In-place modification.
        - Use sorted() for immutability.
    """
    nums = [3, 1, 2]
    nums.sort()
    return nums


# ------------------------------------------------------
def demo_sorted():
    """
    TOPIC:
        sorted(iterable)

    FUNCTION SYNTAX:
        sorted(sequence, key=None, reverse=False)

    USAGE:
        x = [3,1,2]
        y = sorted(x)

    REAL LIFE USECASES:
        - Getting a sorted copy without touching original list.
        - Sorting API results before returning.
        - Safe sorting when sharing lists across components.

    PROS:
        - Returns a NEW list.
        - Works on any iterable.

    CONS:
        - Extra memory allocation.
    """
    x = [3, 1, 2]
    return sorted(x)


# ------------------------------------------------------
def demo_copy():
    """
    TOPIC:
        list.copy()

    FUNCTION SYNTAX:
        list.copy()

    USAGE:
        x = [1,2,3]
        y = x.copy()

    REAL LIFE USECASES:
        - Preventing side-effects.
        - Safe passing of lists into functions.
        - Creating snapshots.

    PROS:
        - Shallow copy, fast.

    CONS:
        - Doesn’t deep copy nested structures.
    """
    x = [1, 2, 3]
    return x.copy()


# ------------------------------------------------------
def demo_membership():
    """
    TOPIC:
        value in list / value not in list

    FUNCTION SYNTAX:
        x in list
        x not in list

    USAGE:
        found = 3 in [1,2,3]

    REAL LIFE USECASES:
        - Permission checks.
        - Searching small caches.
        - Conditional logic.

    PROS:
        - Clean and readable.

    CONS:
        - O(n) lookup. Use set for O(1).
    """
    return 3 in [1, 2, 3]


# ------------------------------------------------------
def demo_slice():
    """
    TOPIC:
        list slicing

    FUNCTION SYNTAX:
        list[start:end:step]

    USAGE:
        x = [0,1,2,3,4]
        part = x[1:4]
        reversed_list = x[::-1]

    REAL LIFE USECASES:
        - Pagination windows.
        - Making copies.
        - Time-series slicing.

    PROS:
        - Highly expressive.
        - Fast and safe.

    CONS:
        - Creates new list → memory cost.
    """
    x = [0, 1, 2, 3, 4]
    return x[1:4]


# ------------------------------------------------------
def demo_aggregates():
    """
    TOPIC:
        max(), min(), sum()

    FUNCTION SYNTAX:
        max(list)
        min(list)
        sum(list)

    USAGE:
        nums = [1,2,3]
        m = max(nums)

    REAL LIFE USECASES:
        - Analytics, stats, score processing.
        - Backend validation (find highest, lowest).

    PROS:
        - Fast, optimized.

    CONS:
        - Works only on numeric or comparable types.
    """
    nums = [1, 2, 3]
    return max(nums), min(nums), sum(nums)


# ------------------------------------------------------
def demo_enumerate():
    """
    TOPIC:
        enumerate(sequence)

    FUNCTION SYNTAX:
        enumerate(iterable, start=0)

    USAGE:
        for i, v in enumerate(['a','b']):
            print(i, v)

    REAL LIFE USECASES:
        - Access index + value in loops.
        - Processing CSV rows.
        - Position tracking.

    PROS:
        - Cleanest index/value iteration.

    CONS:
        - None, this is perfect.
    """
    names = ["hari", "ashik", "ramu"]
    return [(i, v) for i, v in enumerate(names)]
