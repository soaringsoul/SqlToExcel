
# mysql导数辅助小工具

2016年刚刚从事数据分析工作时，因为要频繁的取数，所以使用pyqt5编写的一个mysql导出数据的小工具，

功能很简单，就是将将mysql的查询结果导出为excel或者csv文件。

当时写这个小工具的初衷是给办公室内不会使用sql的同事取数用，另外可以解决直接使用Navicat等工具导出数据时造成的数值格式缺失的问题。

比较简单。不作过多说明。
## 依赖的第三方库

```
pyqt5
pandas
openpyxl
pymysql
sqlalchemy
```

## 使用说明

执行 `python run.py`即可。



![run](/screenshot/run.gif)
