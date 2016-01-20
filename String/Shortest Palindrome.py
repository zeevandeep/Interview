class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        
        tmp=(s+'x')[:-1]
        palindrome= False
        last=''
        last_tmp=''
        chek=''
        while not palindrome:
        
            last_tmp=tmp[-1]
            last+=last_tmp
            chek+=last
            chek+=s
            reverse= chek[::-1]
            if chek==reverse:
                palindrome = True
                print(chek)
                break
            else:
                tmp=tmp[:-1]
                chek=''
k=Solution()
k.shortestPalindrome('abcd')