import markdown
import sys

def main():
    input_md = sys.argv[1]
    output_html = sys.argv[2]
    content = ""
    
    # 入力ファイルから内容を読み取る
    with open(input_md, "r") as f:
        content = f.read()
        
    # MarkdownをHTMLに変換
    content = md_to_html(content)
    
    # 出力ファイルに書き出す
    with open(output_html, "w") as f:
        f.write(content)

# Markdownで書かれた引数contentをHTMLに変換
def md_to_html(content):
    return markdown.markdown(content)

# 実行
main()