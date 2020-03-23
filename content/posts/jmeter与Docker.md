---
title: 'JMeter与Docker'
tags:
  - JMeter
  - Docker
categories:
  - Tool
date: 2017-01-25 21:50:00
---

# JMeter_docker

Use JMeter with Docker

- Replace `Demo.jmx`
- Change the following about `Demo.jmx` file

```
COPY		Demo.jmx /opt/jmeter
```
- build Docker file in root folder

```
docker build -t performanceDocker .
```
- run docker with performance testing

<!--more-->

```
docker run --rm -v $(pwd):/root performanceDocker bin/jmeter -n -t Demo.jmx
```

- The log maybe like this:

```
Writing log file to: /opt/jmeter/jmeter.log
Creating summariser <summary>
Created the tree successfully using Demo.jmx
Starting the test @ Wed Jan 25 02:16:12 UTC 2017 (1485310572802)
Waiting for possible Shutdown/StopTestNow/Heapdump message on port 4445
summary =      1 in 00:00:01 =    1.2/s Avg:   619 Min:   619 Max:   619 Err:     0 (0.00%)
Tidying up ...    @ Wed Jan 25 02:16:13 UTC 2017 (1485310573711)
... end of run
```

## Resource

- Github: [https://github.com/aimer1124/jmeter_docker](https://github.com/aimer1124/jmeter_docker)
- DockerImage: [https://hub.docker.com/r/yjshi/jmeter/](https://hub.docker.com/r/yjshi/jmeter/)
