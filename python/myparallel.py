import time
from concurrent.futures import ThreadPoolExecutor
import sys
import traceback
class myparallel:
	def mysleep3(self,n):
		time.sleep(3)
		return n

	def mysleep5(self,n):
		time.sleep(5)
		return n

	def __init__(self,type):
		# Sequential call
		if type == "s":
			c = self.mysleep5(5) + self.mysleep3(3)
			print(c)

		# Parallel call
		elif type == "p":
			try:
				executor = ThreadPoolExecutor(max_workers=2)
				a = executor.submit(self.mysleep3,30)
				b = executor.submit(self.mysleep5,50)
				d = a.result(timeout=1) + b.result(timeout=10)
				print(d)
				executor.shutdown()

			except Exception as e:
				# Use Logging instead of print
				print("Exception occured:",e.__class__.__name__)
				print("="*10, "Stacktrace", "="*10)
				traceback.print_tb(e.__traceback__)
				print(a.cancel())
				print(b.cancel())
				executor.shutdown()
				err = e

obj = myparallel(sys.argv[1])