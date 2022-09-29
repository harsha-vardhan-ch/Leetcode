class Solution:
    def suggestedProducts(self, products: List[str], search: str) -> List[List[str]]:
        products=sorted(products)
        # print(products)
        res=[]
        # for prod in products:
            
        for i in range(len(search)):
            inres=[]
            for j in products:
                if search[0:i+1]==j[0:i+1]:
                    if len(inres)<3:
                        inres.append(j)
                    else:
                        break
            # print(search[0:i],j[0:i],inres)
            res.append(inres)
        # print(res)
                  
        return res
            