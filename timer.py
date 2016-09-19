import timeit
import os, sys

if __name__ == "__main__":

	loops = 1000 if len(sys.argv) == 1 else int(sys.argv[1])
		
	path = os.path.dirname(os.path.abspath(__file__))

	for path in os.listdir(path):

		if path != "timer.py" and path != ".DS_Store":
			print "\n", path, "loops: ", loops

 			with open(path) as f:
				
				r = f.read()
				print timeit.timeit(r, number=loops)