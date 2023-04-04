from .element import Element	


class HtmlElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		self.chs = []
		for ch in soup.children:
			if ch.name == None:
				from .span import SpanElement
				self.chs.append(SpanElement(ch))
			else:	
				from .factory import get_element
				# print("name child: ",ch.name)
				self.chs.append(get_element(ch))
			
		
	def md(self):
		ret ='<'+self.soup.name+'>'
		for ch in self.chs:
			ret += ch.md()
		ret += '</'+self.soup.name+'>'
		return ret