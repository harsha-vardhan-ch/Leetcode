class Solution:
    def suggestedProducts(self, products: List[str], search: str) -> List[List[str]]:
        
        # Brute Force
        # products=sorted(products)
        # res=[]
        # for i in range(len(search)):
        #     inres=[]
        #     for j in products:
        #         if search[0:i+1]==j[0:i+1]:
        #             if len(inres)<3:
        #                 inres.append(j)
        #             else:
        #                 break
        #     # print(search[0:i],j[0:i],inres)
        #     res.append(inres)
        # return res
    
        # Binary Search
        products.sort() # time O(nlogn)
        array_len = len(products)
        ans = []
        input_char = ""

        for chr in search:
            tmp = []
            input_char += chr
            insertion_index = self.binary_search(products, input_char) # find where input_char can be inserted in-order in the products array
            for word_ind in range(insertion_index, min(array_len, insertion_index+3)): # check the following 3 words, if valid
                if products[word_ind].startswith(input_char):
                    tmp.append(products[word_ind])
            ans.append(tmp)
        return ans

    def binary_search(self, array, target): # bisect.bisect_left implementation
        lo = 0
        hi = len(array)

        while lo < hi:
            mid = (lo + hi) //2
            if array[mid] < target: lo = mid + 1
            else: hi = mid
        return lo
        
            