# express-noti
跟踪快递信息，通过server酱推送

## 说明
1. 利用快递100的接口查询快递

2. 依赖python3和requests库

2. 只是一个简单的单次调用，须配合crontab等定时执行使用。

3. 推送部分实现在main.py的sc_noti()函数里，可以修改实现其他方式推送

## 使用

安装Requests库。示例：

```bash
sudo pip3 install requests
```

拉取代码

```bash
git clone https://github.com/MonsterNone/express-noti.git
```

编辑config.py，填写server酱推送地址
```
cd express-noti
nano config.py
```

测试运行

```bash
python3 main.py
```

加入crontab（或其他）定时执行

```bash
crontab -e

（添加，以下为5分钟获取一次）
*/5 * * * * python3 代码所在绝对路径
```

## 已知问题

快递100的接口在揽件中和已揽件中间更新会有30分钟左右延时
