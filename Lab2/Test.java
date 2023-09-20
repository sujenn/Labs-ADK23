package Lab2;
// A Space efficient Dynamic Programming
// based Java  program to find minimum
// number operations to convert str1 to str2
import java.util.*;
 
class Test {
    // space optimization
    public static int partDist(String w1, String w2, int w1len, int w2len) {
        if (w1len == 0) {
            return w2len;
        }
        if (w2len == 0) {
            return w1len;
        }
    
        int[] prevRow = new int[w2len + 1];
        int[] currRow = new int[w2len + 1];

        for (int j = 0; j < w2len + 1; j++) {
            prevRow[j] = j;
        }

        for (int i = 1; i < w1len + 1; i++) {
            currRow[0] = i;
            for (int j = 1; j < w2len + 1; j++) {
                if (w1.charAt(i - 1) != w2.charAt(j - 1)) {
                    int remove = prevRow[j] + 1;
                    int swap = currRow[j - 1] + 1;
                    int add = prevRow[j - 1] + 1;
                    currRow[j] = Math.min(remove, Math.min(swap, add));
                }
                else {
                    currRow[j] = prevRow[j - 1];
                }
            }
            // Deep copy of currRow to prevRow
            for (int k = 0; k < w2len + 1; k++) {
                prevRow[k] = currRow[k];
            }
        }
 
        return prevRow[w2len];
    }
    public static void main(String[] args)
    {
        String s = "labd";
        String t = "blad";

        int ans = partDist(s, t, 4, 4);
        System.out.println(ans);
    }
}

    
