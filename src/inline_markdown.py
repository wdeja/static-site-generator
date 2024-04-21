import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text == "" or old_node.text is None:
            continue
        links_ = extract_markdown_images(old_node.text)
        if not links_:
            new_nodes.append(old_node)
            continue
        elif len(links_) == 1:
                text_splitted = old_node.text.split(f"![{links_[0][0]}]({links_[0][1]})", 1)
                print(text_splitted)
                print(links_)
                new_nodes.append(TextNode(text_splitted[0],text_type_text))
                new_nodes.append(TextNode(links_[0][0],text_type_image,links_[0][1]))
                new_nodes.append(TextNode(text_splitted[1],text_type_text))
        else:
            text_splitted = [old_node.text]
            for i in range(len(links_)):
                 text_splitted = text_splitted[-1].split(f"![{links_[i][0]}]({links_[i][1]})", 1)
                 new_nodes.append(TextNode(text_splitted[0],text_type_text))
                 new_nodes.append(TextNode(links_[i][0],text_type_image,links_[i][1]))
                 text_splitted = [text_splitted[-1]]
            if text_splitted[-1] != "":
                new_nodes.append(TextNode(text_splitted[0],text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text == "" or old_node.text is None:
            continue
        links_ = extract_markdown_links(old_node.text)
        if not links_:
            new_nodes.append(old_node)
            continue
        elif len(links_) == 1:
                text_splitted = old_node.text.split(f"[{links_[0][0]}]({links_[0][1]})", 1)
                print(text_splitted)
                print(links_)
                new_nodes.append(TextNode(text_splitted[0],text_type_text))
                new_nodes.append(TextNode(links_[0][0],text_type_link,links_[0][1]))
                new_nodes.append(TextNode(text_splitted[1],text_type_text))
        else:
            text_splitted = [old_node.text]
            # print(text_splitted[0])
            # print(text_splitted[-1])
            for i in range(len(links_)):
                 text_splitted = text_splitted[-1].split(f"[{links_[i][0]}]({links_[i][1]})", 1)
                 new_nodes.append(TextNode(text_splitted[0],text_type_text))
                 new_nodes.append(TextNode(links_[i][0],text_type_link,links_[i][1]))
                 text_splitted = [text_splitted[-1]]
            if text_splitted[-1] != "":
                new_nodes.append(TextNode(text_splitted[0],text_type_text))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes,"`",text_type_code)
    nodes = split_nodes_delimiter(nodes,"**",text_type_bold)
    nodes = split_nodes_delimiter(nodes,"*",text_type_italic)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes



tt = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
# print(text_to_textnodes(tt))



# node = TextNode(
#     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     text_type_text,
# )
# new_nodes = split_nodes_image([node])
# print(new_nodes)



# text2 = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
# print(extract_markdown_images(text2))
# [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]

# text3 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# print(extract_markdown_links(text3))
# # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

# node = TextNode("This is text with a `code block` word", text_type_text)
# new_nodes = split_nodes_delimiter([node], "`", text_type_code)
# print(node.__repr__())
# print(new_nodes)
