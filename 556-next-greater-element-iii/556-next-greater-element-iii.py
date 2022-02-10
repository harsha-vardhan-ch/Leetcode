class Solution:
    def nextGreaterElement(self, n: int) -> int:
        '''
        r=str(n)
        if len(r)==1:
            return -1
        m=r[-1]
        m_index=-1
        yz=0
        i=len(r)-1
        for i in range(len(r)-1,0,-1):
            if r[i]<m:
                m_index=i
                print('vhg')
                m=r[i]
            if r[i]>r[i-1]:
                yz=1
                break
        if i==1 and yz==0:
            return -1
        
        print(i,m_index)
        
        h=r[i:m_index]+r[i-1]
        print(h)
        
        new_r=r[:i-1]+r[m_index]+h[::-1]
        
        #print(new_r)
        return int(new_r)
    
        '''
        str_n = str(n)
        digits = [int(i) for i in list(str_n)]

        # find the point at which to begin swap, go from right to left to find the first point of violation
        ptr = len(digits)-1
        while ptr>=1:
            if digits[ptr-1]<digits[ptr]:
                break
            else:
                ptr-=1
        if ptr==0:
            return -1

        # Violation is at ptr-1, now, find exactly once, the first occurrence of next largest element to replace with
        largest_till_now = ptr
        for i in range(ptr+1, len(digits)):
            if digits[i]>digits[ptr-1] and digits[i]<digits[largest_till_now]:
                largest_till_now = i
        digits[ptr-1], digits[largest_till_now] = digits[largest_till_now], digits[ptr-1]

        # now, make sure that this is indeed the next smallest
        # to do so, sort the remaining elements from ptr onwards
        digits[ptr:] = sorted(digits[ptr:])
        result = int(''.join([str(i) for i in digits]))

        # finally, check if this satisfies the bit constraint
        if result.bit_length()<32:
            return result
        else:
            return -1