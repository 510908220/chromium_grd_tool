# chromium_grd_tool
chromium中本地化中文资源添加工具

#为什么会小写一个这样的小工具?
- 比如在基于chromium浏览器上给一个控件添加一个中文:"收藏网页"，默认做法是:
	- 打开[grd](https://www.chromium.org/developers/design-documents/ui-localization)文件创建一个节点,如```  <message name="IDS_NOTE_WEB_PAGE" desc="The text used for note to store web page ">
Store Web Page </message>```
	- 根据desc，使用chromium里一个脚本计算一个id值
	- 然后在中文对应的xtb文件添加一个节点:```<translation id="2452486033108980940">收藏网页</translation>```
- 每次在浏览器上添加一个中文时如此麻烦，而且xtb里的id是不能重复的等等，这些都需要手动检测.


#使用
- 运行grd_web_edit目录下的start.py即可启动（目录下的grd.dat是保存本地添加的记录）
- test_files目录下是测试用的文件，实际的chromium可以修改目录```\grd_web_edit\tools\handler\conf.py```下grd和xtb文件配置.

#实际操作
- 执行start.py会得到如下界面,点击添加:
![](http://7xk7ho.com1.z0.glb.clouddn.com/add.png)
这样一步就解决上述问题.而且还会自动判断重复的。
