class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_self(self):
        raise NotImplementedError("to_html method is not implemented")

    def props_to_html(self):
        if self.props:
            return f'href="{self.props["href"]}" target="{self.props["target"]}"'

    def __repr__(self):
        return f'HTMLNode({self.tag},{self.value},{self.children},{self.props})'