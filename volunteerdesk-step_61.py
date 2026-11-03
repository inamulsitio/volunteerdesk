# === Stage 61: Add performance timing for core list and search operations ===
# Project: VolunteerDesk
import time

def time_operation(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"[timed] {func.__name__}({args}, {kwargs}) = {elapsed*1000:.2f} ms")
    return result

def timed_search(data, predicate, *args, **kwargs):
    start = time.perf_counter()
    matches = [item for item in data if predicate(item, *args, **kwargs)]
    elapsed = time.perf_counter() - start
    print(f"[timed] search({args}, {kwargs}) = {len(matches)} matches in {elapsed*1000:.2f} ms")
    return matches

def timed_list(data, *args, **kwargs):
    start = time.perf_counter()
    result = list(data)
    elapsed = time.perf_counter() - start
    print(f"[timed] list({args}, {kwargs}) = {len(result)} items in {elapsed*1000:.2f} ms")
    return result
