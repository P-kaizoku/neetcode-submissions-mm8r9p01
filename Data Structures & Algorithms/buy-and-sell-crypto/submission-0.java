class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;

        int l=0, r=0;
        while(r<prices.length){
            int profit = prices[r]-prices[l];
            if(prices[l]>prices[r]) l = r;

            maxProfit = (profit>maxProfit)?profit:maxProfit;

            r++;
        }
        return maxProfit;
    }
}
