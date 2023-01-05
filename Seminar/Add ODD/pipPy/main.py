import time

# from progress.bar import Bar
#
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()
# from isOdd import isOdd
#
#
#
# print(isOdd(1))
# print(isOdd(4))
from progress.bar import Bar

with Bar('Processing', max=20) as bar:
    for i in range(5):
        time.sleep(1)
        bar.next()
