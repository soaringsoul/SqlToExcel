---
typora-root-url: ./
---

# mysql导出小工具

2016年时使用pyqt5编写的一个mysql导出数据的小工具，可以将mysql的查询结果导出为excel或者csv文件。

当时写这个小工具的初衷是解决直接使用Navicat等工具导出数据时造成的数值格式缺失的问题。比较简单。不作过多说明。

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