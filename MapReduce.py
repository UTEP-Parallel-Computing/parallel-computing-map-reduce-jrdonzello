import pymp, time, re

class MapReduce():
    words = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet","you", "my","blood","poison","macbeth","king","heart","honest"]
    files = ["shakespeare1.txt","shakespeare2.txt","shakespeare3.txt","shakespeare4.txt","shakespeare5.txt","shakespeare6.txt","shakespeare7.txt","shakespeare8.txt"]

    def main(self):
        #total run time
        start = time.monotonic()
        self.runParallelWC()
        end = time.monotonic() - start
        print('Total runtime: {}'.format(end))

    def runParallelWC(self):
        wordCount = pymp.shared.dict()
        with pymp.Parallel(8) as p:
            lock = p.lock
            for x in self.words:
                wordCount[x] = 0
            for item in p.iterate(self.files):
                start = time.monotonic()
                current_file = open(item, "r")
                current_file = current_file.read()
                # file load time
                end1 = time.monotonic() - start
                for word in self.words:
                    count = re.findall(word, current_file)
                    lock.acquire()
                    wordCount[word] += len(count)
                    lock.release()
                # find words time
                end = time.monotonic() - start
                print('Current file {} on thread num: {}\nOpen/read runtime: {}\nThread runtime: {}'.format(item,p.thread_num,end1,end))
        #print(wordCount)
mapReduce = MapReduce()
mapReduce.main()
