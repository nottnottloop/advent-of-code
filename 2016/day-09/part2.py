# dopamine release a little too high with this solution

import math
import re
import collections

with open('input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

marker_regex = re.compile(r"\((?P<ahead>\d+)x(?P<repeat>\d+)\)")
#count = sum(len(s) for s in re.split(r"\(\d+x\d+\)", line))
count = 0

def find_marker_and_ahead(text):
    marker = re.search(marker_regex, text)
    ahead = ""
    if marker:
        ahead = text[marker.end():marker.end() + int(marker["ahead"])]

    return (marker, ahead)

def find_markers_and_aheads(text):
    markers = list(re.finditer(marker_regex, text))
    aheads = []
    for marker in markers:
        if marker:
            aheads.append(text[marker.end():marker.end() + int(marker["ahead"])])
        else:
            aheads.append("")

    temp_markers_and_aheads = list(zip(markers, aheads))
    markers_and_aheads = []
    lowers_and_highers = []
    for m_a in temp_markers_and_aheads:
        create = True
        if lowers_and_highers:
            for lh in lowers_and_highers:
                if m_a[0].start() > lh[0] and m_a[0].end() < lh[1]:
                    create = False
        if create:
            markers_and_aheads.append(m_a)
            lowers_and_highers.append((m_a[0].start(), m_a[0].end() + len(m_a[1])))
    return markers_and_aheads


i = 0
while i < len(line):
    if not line[i] == "(":
        count += 1
        i += 1
        continue

    print(f"You are {i} out of {len(line)} there ({math.floor((i / len(line)) * 100)}%)")

    marker_list = collections.deque()
    next_marker = find_marker_and_ahead(line[i:])
    next_marker_and_ahead_len = len(next_marker[0].group())+len(next_marker[1])
    marker_list.appendleft(find_markers_and_aheads(line[i:i+next_marker_and_ahead_len])[0])
    i += next_marker_and_ahead_len
    while marker_list:
        main_marker = marker_list.popleft()
        other_markers = find_markers_and_aheads(main_marker[1])
        if not other_markers:
            count += len(main_marker[1] * int(main_marker[0]["repeat"]))
        else:
            to_create = collections.deque()
            for other_marker in other_markers:
                #if len(find_markers_and_aheads(other_marker[1])) == len(other_markers) - 1:
                for j in range(int(main_marker[0]["repeat"])):
                    to_create.appendleft(other_marker)
            marker_list.extendleft(to_create)

    #print(marker_list)
    #break
    #print(markers_and_aheads)


print(f"Final count: {count}")