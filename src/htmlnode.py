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
    
    