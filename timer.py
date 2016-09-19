import timeit
import os, sys

if __name__ == "__main__":

	loops = 1000 if len(sys.argv) == 1 else int(sys.argv[1])
		
	path = os.path.dirname(os.path.abspath(__file__))

	print "loops: ", loops
	print "folder: ", path
	for path in os.listdir(path):

		if path != "timer.py" and path != ".DS_Store":
			print "\n", path

 			with open(path) as f:
				
				r = f.read()
				print "time: ", timeit.timeit(r, number=loops), "secs"