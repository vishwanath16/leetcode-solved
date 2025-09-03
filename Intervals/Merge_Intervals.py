# Link: https://leetcode.com/problems/merge-intervals/description/

def merge(intervals):
    if not intervals:  # Handle empty input
        return []
    
    intervals = sorted(intervals)
    result = [intervals[0]]  # Start with the first interval
    
    for i in range(len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            # Merge by updating the end time of the last interval in result
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            # Add non-overlapping interval to result
            result.append(intervals[i])
    
    return result


print(merge([[1,4],[2,3]]))