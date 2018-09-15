# Python项目：数据可视化
书籍《Python编程：从入门到实践》中的项目2，数据可视化。<br>
Python版本：Python 3.6.3<br>
编译器：PyCharm Community Edition<br>
主要使用到的包：matplotlib，Pygal，pygal_maps_world，requests<br>

简单说明：
## 1.random_walk
>>随机漫步，用Python来生成随机漫步数据，再使用matplotlib以引人瞩目的方式将这些数据呈现出来。随机漫步是这样行走得到的路径：每次行走都完全是随机的，没有明确的方向，结果是由一系列随机决策决定的。你可以这样认为，随机漫步就是蚂蚁在晕头转向的情况下，每次都沿随机的方向前行所经过的路径。<br>
>>效果图如下：<br>
![](https://github.com/Seaworth/Data_visualization/raw/master/random_walk/Figure_1.png)

## 2.Pygal
>>模拟掷两颗骰子D6。<br>
>>创建两个D6骰子，以模拟同时掷两个骰子的情况。程序将这个图表渲染为一个SVG文件，要查看生成的直方图，最简单的方式是使用Web浏览器。Pygal让这个图表具有交互性：如果你将鼠标指向该图表中的任何条形，将看到与之相关联的数据。<br>
>>效果图如下：<br>
![](https://github.com/Seaworth/Data_visualization/raw/master/Pygal/Figure_2.png)
## 3.draw_weather
>>使用Python模块csv 来处理以CSV（逗号分隔的值）格式存储的天气数据，找出两个不同地区在一段时间内的最高温度和最低温度。然后，我们将使用matplotlib根据下载的数据创建一个图表，展示两个不同地区的气温变化。<br>
>>效果图如下：<br>
![](https://github.com/Seaworth/Data_visualization/raw/master/draw_weather/Figure_3.png)
## 4.draw_world_map
>>下载JSON格式的人口数据，并使用json 模块来处理它们。Pygal提供了一个适合初学者使用的地图创建工具包pygal_maps_world，你将使用它来对人口数据进行可视化，以探索全球人口的分布情况。<br>
>>效果图如下：<br>
![](https://github.com/Seaworth/Data_visualization/raw/master/draw_world_map/Figure_4.png)

## 5.Web_API
>>可视化将基于来自GitHub的信息，这是一个让程序员能够协作开发项目的网站。我们将使用GitHub的API来请求有关该网站中Python项目的信息，然后使用Pygal生成交互式可视化，以呈现这些项目的受欢迎程度。<br>
>>效果图如下：<br>
![](https://github.com/Seaworth/Data_visualization/raw/master/Web_API/Figure_5.png)
<br>
## 遇到的坑
>>因为现在第三方的包更新的比较快，有些以前用的包，现在名称已经发生改变。在程序实际的编写过程中，遇到一些问题。<br>
详情可参见链接[绘制世界人口地图遇到的两个问题](https://blog.csdn.net/m0_38059875/article/details/82596992)



