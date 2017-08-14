class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        def getLowestShoppingPrice(price, special, needs, i):
        	if i == len(special):
        		return sum(map(lambda x, y: x*y, needs, price))
        	result = getLowestShoppingPrice(price, special, needs, i+1)
        	for j in range(len(price)):
        		needs[j]-=special[i][j]
        	if all(need>=0 for need in needs):
        		result = min(result, special[i][-1] + getLowestShoppingPrice(price, special, needs, i))
        	for j in range(len(price)):
        		needs[j]+=special[i][j]

        	return result

        print getLowestShoppingPrice(price, special, needs, 0)

    



s = Solution()
price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
s.shoppingOffers(price, special, needs)

