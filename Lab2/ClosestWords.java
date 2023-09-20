package Lab2;
/* Labb 2 i DD2350 Algoritmer, datastrukturer och komplexitet    */
/* Se labbinstruktionerna i kursrummet i Canvas                  */
/* Ursprunglig författare: Viggo Kann KTH viggo@nada.kth.se      */
import java.util.LinkedList;
import java.util.List;

public class ClosestWords {
  LinkedList<String> closestWords = null;

  int closestDistance = -1;

  int partDist2(String w1, String w2, int w1len, int w2len) {
    if (w1len == 0)
      return w2len;
    if (w2len == 0)
      return w1len;
    int res = partDist(w1, w2, w1len - 1, w2len - 1) + 
	(w1.charAt(w1len - 1) == w2.charAt(w2len - 1) ? 0 : 1);
    int addLetter = partDist(w1, w2, w1len - 1, w2len) + 1;
    if (addLetter < res)
      res = addLetter;
    int deleteLetter = partDist(w1, w2, w1len, w2len - 1) + 1;
    if (deleteLetter < res)
      res = deleteLetter;
    return res;
  }

  int partDist(String w1, String w2, int w1len, int w2len) {
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

  int distance(String w1, String w2) {
    return partDist(w1, w2, w1.length(), w2.length());
  }

  public ClosestWords(String w, List<String> wordList) {
    for (String s : wordList) {
      int dist = distance(w, s);
      // System.out.println("d(" + w + "," + s + ")=" + dist);
      if (dist < closestDistance || closestDistance == -1) {
        closestDistance = dist;
        closestWords = new LinkedList<String>();
        closestWords.add(s);
      }
      else if (dist == closestDistance)
        closestWords.add(s);
    }
  }

  int getMinDistance() {
    return closestDistance;
  }

  List<String> getClosestWords() {
    return closestWords;
  }
}