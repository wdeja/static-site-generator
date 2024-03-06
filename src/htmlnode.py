class HTMLNode:
    def __init__(self,
                 tag=None,
                 value=None,
                 children=None,
                 props=None):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        for key in self.props:
            html += f'{key}="{self.props[key]}" '
        return html.rstrip(" ")
    
    def __repr__(self) -> str:
        return f"HTMLNode:{self.tag}, {self.value}, {self.children}, {self.props}"
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children detected")
        html = ""
        for child in self.children:
            html += child.to_html()
        
        if self.props is None:
            return f"<{self.tag}>{html}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__():
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

node = ParentNode(
    "p",
    [
    ],
)


print(node.to_html())

