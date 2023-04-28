import csv
with open('testdata.csv','w')as csvf:
    #建立表头列表
    fieldnames=['prompt','completion']
    writer=csv.DictWriter(csvf,fieldnames=fieldnames)
    writer.writeheader()
    #逐行对应表头写入数据
    writer.writerow({"prompt": "公司:法奥意威，主要出售的机器人是是哪种--", "completion": "法奥五系列,end"})#第一行
    writer.writerow({"prompt": "一个孤独的人会干什么--", "completion": "报军事英语,end"})

