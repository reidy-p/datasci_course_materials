import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    #mr.emit_intermediate((value, key), 1)
    if key > value:
        mr.emit_intermediate((key, value), 1)
    else:
        mr.emit_intermediate((value, key), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) == 1:
        mr.emit((key[0], key[1]))
        mr.emit((key[1], key[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
