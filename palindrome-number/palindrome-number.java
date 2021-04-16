class Solution {
    private int r = 0;
    private int originalNumber = 0;
    private int base = 1;
    
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        originalNumber = x;
        reversedNumber(x);

        if (r == originalNumber) {
            return true;
        }

        return false;
    }

    private void reversedNumber(int x) {
        if (x > 0) {
            reversedNumber((int) Math.floor(x / 10));
            r += (x % 10) * base;
            base *= 10;
        }
    }
}