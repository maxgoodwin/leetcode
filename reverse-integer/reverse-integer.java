class Solution {
    private long r = 0;
    private long base = 1;
    public int reverse(int x) {

        boolean positive = true;
        if (x < 0) {
            positive = false;
            x = Math.abs(x);
        }

        if (x > 0) {
            reverse((int) Math.floor(x/10.00));
            int lastDigit = x % 10;
            r += lastDigit * base;
            base *= 10;
        }

        if (positive == false) {
            r = r - r * 2;
        }

        if (Math.abs(r) > Integer.MAX_VALUE) {
            return 0;
        }

        return (int) r;
    }
}