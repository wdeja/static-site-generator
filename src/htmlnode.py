text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class HTMLNode:
    def __init__(self,
                    tag: str=None,
                    value:str=None,
                    children:list=None,
                    props:dict=None) -> None:
            
            self.tag = tag
            self.value = value
            self.children = children
            self.props = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        result = ""
        if self.props is not None:
            for prop in self.props:
                result += f" {prop}=\"{self.props[prop]}\""
        return result.rstrip()
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def text_node_to_html_node(text_node):
        pass

    
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, value: str = "", props: dict[str,str] | None = None) -> None:
        super().__init__(tag=tag,value=value, props=props)
        
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
             return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> None:
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("Different message")
        result = ""
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

        

          





def main():
    a = HTMLNode("a","b",props={"href": "https://www.google.com", "target": "_blank"})
    print(a.props_to_html())
    print(a.__repr__())
    b = LeafNode("a","b")


    c =LeafNode()
    d = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    e = LeafNode(value = "This is plain text")

    node = ParentNode(
    "p",    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
) 

    print(node.to_html())
    print(c.to_html())
    # print(e.to_html())

if __name__ == "__main__":
    main()