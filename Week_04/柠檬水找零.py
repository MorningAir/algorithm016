class Solution:
    def lemonadeChange(self, bills):
        i = 0
        j = 0
        for k in range(len(bills)):
            if bills[k] == 5:
                i += 1
                print('收5元')
            elif bills[k] == 10:
                i -= 1
                j += 1
                print('收10元找5元')
            else:
                if j >= 1:
                    i -= 1
                    j -= 1
                    print('收20元，找10+5元')
                else:
                    i -= 3
                    print('收20元，找5+5+5元')
            print(i,j)
            if i < 0 or j < 0:
                return False
        return True
s = Solution()
print(s.lemonadeChange([5,5,10,10,20]))