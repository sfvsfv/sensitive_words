参考来自：中华人民共和国审查辞汇列表

链接：https://zh.wikiversity.org/zh-hans/%E4%B8%AD%E8%8F%AF%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9C%8B%E5%AF%A9%E6%9F%A5%E8%BE%AD%E5%BD%99%E5%88%97%E8%A1%A8


更多敏感词，请参考：
https://chinadigitaltimes.net/space/CDS%E4%B8%93%E9%A1%B5%EF%BC%9A%E6%95%8F%E6%84%9F%E8%AF%8D%E5%BA%93


敏感词检测：

```clike
your_text = """
一夜情的故事
"""

# 打开并读取min_word_processed.txt文件
with open('min_word_processed.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 移除每行末尾的换行符并存储
processed_lines = [line.strip() for line in lines]

# 检查每一行是否出现在文本中
for line in processed_lines:
    if line in your_text:
        print(f"找到匹配项: {line}")

```
如下所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b9176097a09e49e193626f9060f5a98a.png)
即使几万个敏感词，不到一秒钟即可匹配出来！
