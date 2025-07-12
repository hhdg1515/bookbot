def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

def get_sorted_char_list(char_counts):
    # 转换字典为列表，每个元素是 {'char': 字符, 'num': 计数}
    char_list = [{"char": c, "num": n} for c, n in char_counts.items()]
    # 按 'num' 从大到小排序
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
