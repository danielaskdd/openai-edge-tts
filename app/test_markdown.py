import re

def test_heading_processing():
    test_cases = [
        (
            "# 一级标题\n## 二级标题\n### 三级标题",
            "一级标题\n二级标题\n三级标题"
        ),
        (
            "#不是标题\n# 是标题",
            "#不是标题\n是标题"
        ),
        (
            "# 标题1\n正常文本\n## 标题2",
            "标题1\n正常文本\n标题2"
        )
    ]

    def process_text(text):
        return re.sub(r'^#+\s', '', text, flags=re.MULTILINE)

    for i, (input_text, expected_output) in enumerate(test_cases, 1):
        result = process_text(input_text)
        success = result == expected_output
        print(f"\n标题处理测试 {i}:")
        print(f"输入:\n{input_text}")
        print(f"期望:\n{expected_output}")
        print(f"实际:\n{result}")
        print(f"结果: {'通过' if success else '失败'}")

def test_list_processing():
    test_cases = [
        (
            "* 列表项1\n* 列表项2\n  * 子列表项",
            "列表项1\n列表项2\n子列表项"
        ),
        (
            "> * 引用中的列表\n* 普通列表",
            "引用中的列表\n普通列表"
        )
    ]

    def process_text(text):
        return re.sub(r'(?:^\s*\*\s|^>\s+\*\s)', '', text, flags=re.MULTILINE)

    for i, (input_text, expected_output) in enumerate(test_cases, 1):
        result = process_text(input_text)
        success = result == expected_output
        print(f"\n列表处理测试 {i}:")
        print(f"输入:\n{input_text}")
        print(f"期望:\n{expected_output}")
        print(f"实际:\n{result}")
        print(f"结果: {'通过' if success else '失败'}")

def test_code_block_processing():
    test_cases = [
        (
            "```python\nprint('hello')\n```",
            "省略python代码块"
        ),
        (
            "```\ncode here\n```",
            "省略代码块"
        ),
        (
            "    code line1\n    code line2",
            "省略代码块\n"
        ),
        (
            "正常文本\n    缩进代码\n    继续缩进\n正常文本",
            "正常文本\n省略代码块\n正常文本"
        )
    ]

    def process_text(text):
        # 处理带有语言类型的代码块
        text = re.sub(r'^```(\w+).*\n[\s\S]*?^```', r'省略\1代码块', text, flags=re.MULTILINE)
        # 处理不带语言类型的代码块
        text = re.sub(r'^```.*\n[\s\S]*?^```', '省略代码块', text, flags=re.MULTILINE)
        # 处理缩进式代码块
        text = re.sub(r'(?:(?:^[ ]{4}|\t).*(?:\n|$))+(?:\n)?', '省略代码块\n', text, flags=re.MULTILINE)
        return text

    for i, (input_text, expected_output) in enumerate(test_cases, 1):
        result = process_text(input_text)
        success = result == expected_output
        print(f"\n代码块处理测试 {i}:")
        print(f"输入:\n{input_text}")
        print(f"期望:\n{expected_output}")
        print(f"实际:\n{result}")
        print(f"结果: {'通过' if success else '失败'}")

def test_underscore_processing():
    test_cases = [
        (
            "正常文本 _____ 后面文本",
            "正常文本 __ 后面文本"
        ),
        (
            "文本1 __ 文本2 ______ 文本3",
            "文本1 __ 文本2 __ 文本3"
        )
    ]

    def process_text(text):
        return re.sub(r'_{2,}', '__', text, flags=re.MULTILINE)

    for i, (input_text, expected_output) in enumerate(test_cases, 1):
        result = process_text(input_text)
        success = result == expected_output
        print(f"\n下划线处理测试 {i}:")
        print(f"输入: {input_text}")
        print(f"期望: {expected_output}")
        print(f"实际: {result}")
        print(f"结果: {'通过' if success else '失败'}")

def test_bracket_processing():
    # 测试用例
    test_cases = [
        (
            "这是一个[测试]文本",
            "这是一个文本"
        ),
        (
            "这是一个[链接文本](http://example.com)测试",
            "这是一个链接文本测试"
        ),
        (
            "多个测试：[测试1][测试2][链接](http://test.com)",
            "多个测试：链接"
        ),
        (
            "混合测试[测试1]text[链接1](link1)[测试2][链接2](link2)",
            "混合测试text链接1链接2"
        )
    ]

    def process_text(text):
        # 从server.py复制的处理逻辑
        # 1. 如果中括号后面没有紧跟小括号,则删除中括号及其内容
        text = re.sub(r'\[[^\]]*\](?!\([^\)]*\))', '', text)
        # 2. 如果中括号后面紧跟小括号,则保留中括号内容,删除小括号及其内容
        text = re.sub(r'\[([^\]]*)\](?=\([^\)]*\))\([^\)]*\)', r'\1', text)
        return text

    # 运行测试
    for i, (input_text, expected_output) in enumerate(test_cases, 1):
        result = process_text(input_text)
        success = result == expected_output
        print(f"\n测试用例 {i}:")
        print(f"输入: {input_text}")
        print(f"期望: {expected_output}")
        print(f"实际: {result}")
        print(f"结果: {'通过' if success else '失败'}")

if __name__ == '__main__':
    print("\n开始测试标题处理逻辑...")
    test_heading_processing()
    
    print("\n开始测试列表处理逻辑...")
    test_list_processing()
    
    print("\n开始测试代码块处理逻辑...")
    test_code_block_processing()
    
    print("\n开始测试下划线处理逻辑...")
    test_underscore_processing()
    
    print("\n开始测试中括号处理逻辑...")
    test_bracket_processing()
