def count_line_changes(lines):
    count = 0
    prevLine = lines[0]
    for i in range(len(lines)):
        if lines[i] != prevLine:
            count = count+1
        prevLine = lines[i]
    return count


def station_ranker(list):
  rankedList = []
  for i in list:
    line_count = count_line_changes(i["lines"])
    time = ((int(i["path_size"])-line_count-1) * 3) + (line_count*8)
    rankedList.append({"time":time,"paths":i["paths"],"lines":i["lines"]})
  
  rankedList.sort(key=lambda x: x["time"], reverse=False)
  return rankedList