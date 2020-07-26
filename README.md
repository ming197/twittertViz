# twittertViz
Visulization of Wuhan Lab on Twitter 
# Wuhan Lab 事件推特分析

## 1. 数据收集

本次研究主要是对推特平台上的 Wuhan Lab 事件进行分析。收集的数据主要包括两个部分：（1）与 Wuhan Lab 相关的推文信息；（2）上述推文的转发者ID以及转发者信息。

### 1.1 推文数据

此部分主要收集了推特上关于 Wuhan Lab的推文信息，时间跨度为：2020-01-23 至 2020-05-31。数据收集的具体过程为：通过 python 脚本文件和  selenium 工具，并以 “wuhan lab” 为关键词，转发数大于等于40为限定条件，搜索每天与wuhan lab相关的推文并爬取推文信息。推文数据的具体内同包括：推文链接，发推者的screen_name，发推时间，推文内容，推文转发数等。

### 1.2 转发者信息

由于需要研究推特上Wuhan Lab事件的发展过程，我们需要收集每条推文转发者的信息，并分析转发者之间的关系。此处，我们通过 [Twrench](https://pickaw.app/) 收集了每条推文的转发信息，并通过 [Twitter API](https://developer.twitter.com/en) 收集了每位转发者的相关信息。

## 2. 数据处理

为了研究 Wuhan Lab 事件在推特上的发展，我们对每日的 Wuhan Lab相关推文转发数，转发者的粉丝数进行了统计，分析 Wuhan Lab 事件在推特的传播发展趋势。

通过上一步的统计分析，我们得到了 Wuhan Lab 事件发展的几个关键节点，并对这几个关键的时间节点作进一步的分析。为了分析每日不同推特之间的关系，我们将发推着与转推者之间的关系用有向图表示，分析了不同推特的转发者之间的关系。

### 3. 可视化处理

将 2 中分析处理得到的数据用Gephi软件做可视化分析，得到推特上 Wuhan Lab事件每日的传播关系图。



