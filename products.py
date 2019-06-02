class Product():
    def __init__(self, div):
        info=[]
        self.THC = 'N/A'
        self.CBD = 'N/A'
        self.price = 'N/A'
        self.name = 'failed to parse'
        childern = div.findChildren('span')
        for c in childern:
            text=(c.getText().strip())
            if 'THC' in text:
                self.THC=text
            if 'CBD' in text:
                self.CBD=text
            if '$' in text:
                self.price=text
            if text.isupper():
                self.name=text
            info.append(text)
        self.type=info[0]


    def __str__(self):
        string='Product Name: %s \n' \
               'THC content:  %s \n' \
               'CBD content:  %s \n' \
               'Price:        %s'
        return string %(self.name,self.THC, self.CBD, self.price)
