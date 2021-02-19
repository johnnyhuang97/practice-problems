from itertools import combinations

# PART1
# get common courses taken by all possible pairs of students
input1 = [["58", "A"], ["94", "B"], ["17", "A"], ["58", "B"], ["17", "B"], ["58", "C"]]
def findpair(input):
  mp = {}
  courses = set()
  students = set()
  for student, course in input:
    mp.setdefault(student, set()).add(course)
    courses.add(course)
    students.add(student)

  pairs = combinations(students, 2)
  res = dict()
  for p in pairs:
    s1 = p[0]
    s2 = p[1]
    res[p] = list(mp[s1] & mp[s2])
  for k in res:
    print(k, ":" , res[k])



from collections import defaultdict
#PART 2
#Given course path, find halfway. (courses only have 1 pre reqs)
input2 = [["A", "B"], ["C", "D"], ["B", "C"], ["E", "F"], ["D", "E"], ["F", "G"]] 
def findMidCourse(input):
  count = defaultdict(int)
  path = dict()

  for start,end in input:
    path[start] = end
    count[start] += 1
    count[end] += 1
  
  endpts = [x for x in count.keys() if count[x] == 1]
  begin = endpts[0] if endpts[0] in path.keys() else endpts[1]

  mid = len(path.keys()) // 2
  while mid > 0:
    begin = path[begin]
    mid -= 1
  return begin

#findMidCourse(input2)

def backtrack(src, graph, temp, res):
  childs = graph[src]
  n = len(childs)
  if n == 0:
    res.add(temp[(len(temp)+1)// 2 - 1])
    return res
  
  for i in range(n):
    nxt = graph[src][i]
    temp.append(nxt)
    res = backtrack(nxt, graph, temp, res)
    temp.pop()
  return res

def part3(input):
  parents = defaultdict(int)
  graph = {}

  for src,des in input:
    graph.setdefault(src, list()).append(des)

    if des not in graph:
      graph[des] = list()
    
    if src not in parents:
      parents[src] = 0
    
    parents[des] += 1
  
  res = set()
  for key in parents.keys():
    if parents[key] == 0:
      temp = []
      temp.append(key)
      res = backtrack(key, graph, temp, res)
  print(res)


  
input3 = [ [ "Logic", "COBOL" ], [ "Data Structures", "Algorithms" ], [ "Creative Writing", "Data Structures" ], [ "Algorithms", "COBOL" ], [ "Intro to Computer Science", "Data Structures" ], [ "Logic", "Compilers" ], [ "Data Structures", "Logic" ], [ "Creative Writing", "System Administration" ], [ "Databases", "System Administration" ], [ "Creative Writing", "Databases" ], [ "Intro to Computer Science", "Graphics" ], ["COBOL", "Compilers"] ]
part3(input3)

