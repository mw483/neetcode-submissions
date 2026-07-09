from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Nested dictionary
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # Return "" if key does not exist
        if key not in self.m:
            return ""
        
        # Let times be the sorted list of timestamps for this key
        # Use binary search on times to find the rightmost index i such that times[i] <= timestamp
        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1

        # If such an index exist, return the value associated with times[i]
        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        
        # Otherwise return ""
        return ""
        
