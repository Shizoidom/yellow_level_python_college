class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        for current in intervals:
            if not merged or merged[-1][1] < current[0]:
                merged.append(current)
            else:
                merged[-1][1] = max(merged[-1][1], current[1])

        return merged
