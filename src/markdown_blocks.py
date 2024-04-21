block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block[0] == "#" and len(block.lstrip(" ").split(" ")[0]) < 7:
        return block_type_heading
    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    for line in block.split("\n"):
        if line[0] != ">":
            break
    else:
        return block_type_quote
    for line in block.split("\n"):
        if line[:2] != "* " and line[:2] != "- ":
            break
    else:
        return block_type_unordered_list
    for i, line in enumerate(block.split("\n")):
        if line[:2] != f"{i+1}.":
            print(i)
            break
    else:
        return block_type_ordered_list
    return block_type_paragraph




aa = """1.This is **bolded** paragraph

1.This is another paragraph with *italic* text and `code` here
2.This is the same paragraph on a new line

* This is a list
* with items"""

for block in markdown_to_blocks(aa):
    print(block_to_block_type(block))