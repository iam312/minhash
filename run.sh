cd lib

hadoop fs -rm /user/sammy/output/*
hadoop fs -rmdir /user/sammy/output
hadoop jar /usr/local/Cellar/hadoop/2.4.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.4.0.jar \
          -file seeds.py \
          -file minhash.py \
          -file seed.txt \
          -input test.txt \
          -output output \
          -mapper mapper.py  \
          -reducer /bin/cat
