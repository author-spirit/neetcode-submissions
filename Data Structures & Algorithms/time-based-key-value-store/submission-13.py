class TimeMap:

    def __init__(self):
        # Store it in groups with multiple version
        self.datastore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.datastore.get(key):
            self.datastore[key] = []
            
        self.datastore[key].append({"value": value, "ts": timestamp})

    def get(self, key: str, timestamp: int) -> str:
        if not self.datastore.get(key):
            return ""
        
        # if available check against the previous
        prev = self.datastore[key][-1]

        if prev['ts'] <= timestamp:
            return prev['value']

        # search version (less than prev, equal to timestamp)
        versions = self.datastore[key]

        left = 0
        right = len(versions) - 1
        
        res = ""
        while left <= right:
            mid = (left + (right))//2
            mid_ts = versions[mid]['ts']

            if mid_ts == timestamp:
                return versions[mid]['value']
            elif mid_ts > timestamp:
                right = mid - 1
            else:
                res = versions[mid]['value']
                left = mid + 1
        
        return res

        
