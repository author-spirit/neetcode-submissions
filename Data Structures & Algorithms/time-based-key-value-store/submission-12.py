class TimeMap:

    def __init__(self):
        # Store it in groups with multiple version
        self.datastore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.datastore.get(key):
            self.datastore[key] = {"prev": timestamp, "values": [{"value": value, "ts": timestamp}]}
        else:
            self.datastore[key]["prev"] = timestamp
            self.datastore[key]["values"].append({"value": value, "ts": timestamp})

    def get(self, key: str, timestamp: int) -> str:
        if not self.datastore.get(key):
            return ""
        
        # if available check against the previous
        prev = self.datastore[key]['prev']

        if prev <= timestamp:
            return self.datastore[key]['values'][-1]['value']

        # search version (less than prev, equal to timestamp)
        versions = self.datastore[key]['values']

        left = 0
        right = len(versions) - 1
        
        res = ""
        while left <= right:
            mid = (left + (right))//2
            mid_ts = versions[mid]['ts']

            # print(f"mid={mid}, mid_ts={mid_ts}, ts={timestamp}")

            if mid_ts == timestamp:
                return versions[mid]['value']
            elif mid_ts > timestamp:
                right = mid - 1
            else:
                res = versions[mid]['value']
                left = mid + 1
        
        return res

        
