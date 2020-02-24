Assignment 2 Map Reduce Report
From Justen Donzello

The biggest problem I had doing this assignment was creating the parallel version of the algorithm.
I understood the problem and how to solve it thoroughly, I was able to write a serial in a little less than an hour.
But when it came down to implementing a parallel version, I had trouble structuring my code to be able to work properly.
I went back and look at the examples provided on github and that helped.

Another problem I had was figuring out where to place the time functions in order to record the runtime of my code.
This problem may still reside in my code and I am not sure whether or not the placement provides the correct time.
I do not know if this is the root of another problem but my program does not seem improve with the addition of new threads.
I was fairly confident about how I laid out my code but I code not find/understand why this happens.

I worked on this assignment for about 3-4 hours. I wrote the code in about 2-2.5 hours, converting my serial version to parallel and finding the components we needed to parallelize.

Performance Stats:
I have a separate document (PerformaceStatsJD.pdf) with the stats of each one

I thought that the runtime for loading the file and finding all the words would remain constant no matter how many threads you add.
I came to this conclusion because the file and the number of words never changes so I assumed the time would remain constant.
I also thought that the total time of the program would decrease with each addition of threads because we could partition the program better/more efficiently, making it faster.
But when I actually ran my program nothing seemed to improve and the time remained constant. I do not quite understand how this happens, you can see how it is still partitioned to new threads but nothing still improves.
