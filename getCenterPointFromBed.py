import sys

def parseBed(fname):
  data = []
  with open(fname) as f:
    data = [l.strip().split() for l in f]
  return data

def extractRelevantFields(bed_list):
  """Extract fields: e[0] (chromosome), centerpoint of bed interval 
      e[5] (strandedness), and return as
     list of tuples."""
  return [tuple([e[0], (int(e[1]) + int((int(e[2]) - int(e[1])) / 2)), e[5]]) for e in bed_list]

def main():
  if len(sys.argv) != 2:
    print("Usage: <exe> <bed_file.bed>")
    sys.exit(1)

  center_points = extractRelevantFields(parseBed(sys.argv[1]))
  with open(sys.argv[1][:-4]+".bcp", 'w') as f:
    f.write("\n".join([",".join([c, str(cp), s]) for c, cp, s in center_points]))

if __name__ == '__main__':
  main()
