def canschedule(meetings, start, end):
  for meeting in meetings:
    if start < meeting[1] and end > meeting[0]:
      return False
  return True

meetings = [[1300,1500],[930, 1300], [830,845]]
#print(canschedule(meetings, 845, 900))

def mergeintervals(meetings):
  meetings.sort(key = lambda x: x[0])
  #print(meetings)
  if len(meetings) <= 1:
    return meetings

  merged = list()
  merged.append(meetings[0])

  for i in range(1, len(meetings)):
    meeting = meetings[i]
    if meeting[0] <= merged[-1][1]:
      merged[-1][1] = max(merged[-1][1], meeting[1])
    else:
      merged.append(meeting)
  
  return merged
#print(mergeintervals(meetings))
def sparetime(meetings):
  merged = mergeintervals(meetings)
  res = []
  start = 0

  for i in range(len(merged)):
    if (merged[i][0] > start):
      res.append([start,merged[i][0]])
    start = merged[i][1]
  
  if start < 2400:
    res.append([start, 2400])
  return res
print(sparetime(meetings))
