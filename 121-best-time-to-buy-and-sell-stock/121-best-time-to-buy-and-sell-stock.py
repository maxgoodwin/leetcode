class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    minPrices = []
    currMinPrice = 10001
    profit = 0
    
    for price in prices:
      minPrices.append(currMinPrice)
      if price < currMinPrice: currMinPrice = price
    
    for minPrice, price in zip(minPrices, prices):
      profit = max(profit, price - minPrice)
        
    return profit