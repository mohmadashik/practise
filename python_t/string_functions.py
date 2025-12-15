"""
MODULE: string_notes
Purpose: Inbuilt string operations with consistent docstring structure:
topic, function syntax, usage (this is CODE), real life usecases, pros, cons.
"""


# ------------------------------------------------------
def demo_len():
    """
    TOPIC:
        len(string)

    FUNCTION SYNTAX:
        len(sequence)

    USAGE:
        s = "hello"
        n = len(s)

    REAL LIFE USECASES:
        - Validate password length.
        - Check input size limits.
        - Truncate or paginate text.

    PROS:
        - O(1), extremely fast.

    CONS:
        - Counts characters, not words.
    """
    return len("hello")


# ------------------------------------------------------
def demo_lower_upper():
    """
    TOPIC:
        string.lower(), string.upper()

    FUNCTION SYNTAX:
        str.lower()
        str.upper()

    USAGE:
        s = "Ashik"
        s1 = s.lower()
        s2 = s.upper()

    REAL LIFE USECASES:
        - Case-insensitive comparisons.
        - Normalizing usernames/emails.
        - Search and indexing.

    PROS:
        - Simple and safe.
        - Returns new string (immutable).

    CONS:
        - Locale-specific edge cases (rare).
    """
    s = "Ashik"
    return s.lower(), s.upper()


# ------------------------------------------------------
def demo_strip():
    """
    TOPIC:
        string.strip(), lstrip(), rstrip()

    FUNCTION SYNTAX:
        str.strip(chars)
        str.lstrip(chars)
        str.rstrip(chars)

    USAGE:
        s = "  hello  "
        clean = s.strip()

    REAL LIFE USECASES:
        - Cleaning user input.
        - Removing newline/whitespace from files.
        - Sanitizing API payloads.

    PROS:
        - Very common.
        - Prevents subtle bugs.

    CONS:
        - Only removes from ends, not middle.
    """
    s = "  hello  "
    return s.strip(), s.lstrip(), s.rstrip()


# ------------------------------------------------------
def demo_split():
    """
    TOPIC:
        string.split()

    FUNCTION SYNTAX:
        str.split(sep=None, maxsplit=-1)

    USAGE:
        s = "a,b,c"
        parts = s.split(",")

    REAL LIFE USECASES:
        - Parse CSV-like strings.
        - Tokenize user input.
        - Break logs into fields.

    PROS:
        - Very powerful and flexible.

    CONS:
        - Complex delimiters may need regex.
    """
    s = "a,b,c"
    return s.split(",")


# ------------------------------------------------------
def demo_join():
    """
    TOPIC:
        string.join()

    FUNCTION SYNTAX:
        sep.join(iterable)

    USAGE:
        parts = ["a", "b", "c"]
        s = ",".join(parts)

    REAL LIFE USECASES:
        - Build CSV strings.
        - Construct SQL queries safely (with params).
        - Generate paths or messages.

    PROS:
        - Much faster than string concatenation in loops.

    CONS:
        - Iterable must contain only strings.
    """
    parts = ["a", "b", "c"]
    return ",".join(parts)


# ------------------------------------------------------
def demo_replace():
    """
    TOPIC:
        string.replace()

    FUNCTION SYNTAX:
        str.replace(old, new, count=-1)

    USAGE:
        s = "hello world"
        s2 = s.replace("world", "ashik")

    REAL LIFE USECASES:
        - Mask sensitive data.
        - Template substitutions.
        - Cleanup logs.

    PROS:
        - Simple and readable.

    CONS:
        - No regex support (use re.sub for that).
    """
    s = "hello world"
    return s.replace("world", "ashik")


# ------------------------------------------------------
def demo_find_index():
    """
    TOPIC:
        string.find() vs string.index()

    FUNCTION SYNTAX:
        str.find(sub)
        str.index(sub)

    USAGE:
        s = "hello"
        a = s.find("e")    # 1
        b = s.find("x")    # -1

    REAL LIFE USECASES:
        - Substring search.
        - Validate patterns in strings.

    PROS:
        - find() is safe (no exception).

    CONS:
        - index() throws ValueError if not found.
    """
    s = "hello"
    return s.find("e"), s.find("x")


# ------------------------------------------------------
def demo_startswith_endswith():
    """
    TOPIC:
        string.startswith(), string.endswith()

    FUNCTION SYNTAX:
        str.startswith(prefix)
        str.endswith(suffix)

    USAGE:
        s = "file.txt"
        is_txt = s.endswith(".txt")

    REAL LIFE USECASES:
        - File type checks.
        - URL/path validation.
        - Routing logic.

    PROS:
        - Very readable.
        - Faster than slicing.

    CONS:
        - Exact match only (no patterns).
    """
    s = "file.txt"
    return s.startswith("file"), s.endswith(".txt")


# ------------------------------------------------------
def demo_is_methods():
    """
    TOPIC:
        string is* methods (isalnum, isalpha, isdigit, isspace)

    FUNCTION SYNTAX:
        str.isalnum()
        str.isalpha()
        str.isdigit()
        str.isspace()

    USAGE:
        s = "123"
        check = s.isdigit()

    REAL LIFE USECASES:
        - Input validation.
        - OTP / PIN checks.
        - Sanitizing form data.

    PROS:
        - Very useful for validation.
        - No regex needed.

    CONS:
        - Unicode quirks (e.g., non-ASCII digits).
    """
    return (
        "123".isdigit(),
        "abc".isalpha(),
        "abc123".isalnum(),
        "   ".isspace()
    )


# ------------------------------------------------------
def demo_format_fstring():
    """
    TOPIC:
        string formatting (format, f-string)

    FUNCTION SYNTAX:
        str.format()
        f"{var}"

    USAGE:
        name = "Ashik"
        s1 = "Hello {}".format(name)
        s2 = f"Hello {name}"

    REAL LIFE USECASES:
        - Logging.
        - User-facing messages.
        - Dynamic SQL (with care).

    PROS:
        - f-strings are fastest and cleanest.

    CONS:
        - f-strings evaluate immediately (no lazy eval).
    """
    name = "Ashik"
    return "Hello {}".format(name), f"Hello {name}"


# ------------------------------------------------------
def demo_membership():
    """
    TOPIC:
        substring membership

    FUNCTION SYNTAX:
        sub in string
        sub not in string

    USAGE:
        s = "hello world"
        check = "world" in s

    REAL LIFE USECASES:
        - Keyword detection.
        - Content filtering.
        - Routing rules.

    PROS:
        - Clean and Pythonic.

    CONS:
        - Case-sensitive by default.
    """
    return "world" in "hello world"


# ------------------------------------------------------
def demo_slice():
    """
    TOPIC:
        string slicing

    FUNCTION SYNTAX:
        string[start:end:step]

    USAGE:
        s = "abcdef"
        part = s[1:4]
        rev = s[::-1]

    REAL LIFE USECASES:
        - Masking data (credit cards).
        - Extract tokens.
        - Reverse strings.

    PROS:
        - Very fast and expressive.

    CONS:
        - Creates new string (immutability).
    """
    s = "abcdef"
    return s[1:4], s[::-1]
