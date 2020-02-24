import pymp, time, re

class MapReduce():
    words = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet","you", "my","blood","poison","macbeth","king","heart","honest"]
    files = ["shakespeare1.txt","shakespeare2.txt","shakespeare3.txt","shakespeare4.txt","shakespeare5.txt","shakespeare6.txt","shakespeare7.txt","shakespeare8.txt"]

    def main(self):
        #total run time
        start = time.process_time()
        self.runParallelWC()
        end = time.process_time() - start
        print('Total runtime: {}'.format(end))


    def runParallelWC(self):
        wordCount = pymp.shared.dict()
        with pymp.Parallel(2) as p:
            lock = p.lock
            for x in self.words:
                wordCount[x] = 0
            for item in p.iterate(self.files):
                start = time.process_time()
                current_file = open(item, "r")
                current_file = current_file.read()
                for word in self.words:
                    count = re.findall(word, current_file)
                    lock.acquire()
                    wordCount[word] += len(count)
                    lock.release()
                end = time.process_time() - start
                print('Thread num {} - Current file {} runtime: {}'.format(p.thread_num,item,end))
        #print(wordCount)
mapReduce = MapReduce()
mapReduce.main()
