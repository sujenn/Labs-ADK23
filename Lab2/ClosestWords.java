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
    int[][] editMatrix = new int[w2len + 1][w1len + 1];

    for (int row = 0; row < w2len + 1; row++) {
        editMatrix[row][0] = row;
    }
    for (int col = 1; col < w1len + 1; col++) {
    editMatrix[0][col] = col;
    }

    for (int col = 1; col < w1len + 1; col++) {
      for (int row = 1; row < w2len + 1; row++) {
        if (w1.charAt(col - 1) != w2.charAt(row -1)){
          int remove = editMatrix[row][col - 1] + 1;
          int swap = editMatrix[row - 1][col] + 1;
          int add = editMatrix[row - 1][col - 1] + 1;
          if (row + 1 < w2len + 1){
            editMatrix[row][col] = Math.min(remove, Math.min(swap, add));
          }
        } else{
          editMatrix[col][row] =  editMatrix[col - 1][row - 1];
        }
      }     
    }
    for(int col = 0; col < w2len +1; col++){
      for(int row = 0; row < w1len + 1; row++){
        System.out.print(editMatrix[row][col] + " ");
      }
      System.out.println();
    }

    return editMatrix[w2len + 1][w1len + 1]; //kanske +1??
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