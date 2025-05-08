import os

def find_md_without_pdf(root_dir):
    missing_pdf_dirs = []

    for dirpath, _, filenames in os.walk(root_dir):
        if 'index.md' in filenames:
            file_path = os.path.join(dirpath, 'index.md')
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if "PDF" not in content:
                missing_pdf_dirs.append(dirpath)

    return missing_pdf_dirs

# 使用方法
root_directory = "/Users/bibaolong/Desktop/ict/hugo/bgt-m.github.io/content/publication"  # 替换为你的路径
missing_dirs = find_md_without_pdf(root_directory)

# 打印结果
print("以下文件夹中的 index.md 不含 'PDF':")
for d in missing_dirs:
    print(d)
