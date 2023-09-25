package Lab2;
/* Labb 2 i DD2350 Algoritmer, datastrukturer och komplexitet    */
/* Se labbinstruktionerna i kursrummet i Canvas                  */
/* Ursprunglig författare: Viggo Kann KTH viggo@nada.kth.se      */
import java.util.LinkedList;
import java.util.List;

public class ClosestWords {
  LinkedList<String> closestWords = null;
  int closestDistance = -1;
  int[][] editMatrix = new int[200][200];
  String oldWord = "";

  int partDist(String w1, String w2, int w1len, int w2len) {  //w1 är det ord som är felstavat och w2 är ordet som finns i ordlistan
    if (w1len == 0) {
        return w2len;
    }
    if (w2len == 0) {
        return w1len;
    }

    int changeFromRow = 0;
    int compare = 0;
    while (compare < Math.min(w2len, oldWord.length())) {
      if (w2.charAt(compare) != oldWord.charAt(compare)) {
        break;
      }
      changeFromRow++;
      compare++;
    }

    for (int row = 0; row < w2len + 1; row++) {
      editMatrix[row][0] = row;
    }
    for (int col = 1; col < w1len + 1; col++) {
      editMatrix[0][col] = col;
    }

    for (int row = changeFromRow + 1; row < w2len + 1; row++) {
      for (int col = 1; col < w1len + 1; col++) {
        if (w2.charAt(row - 1) != w1.charAt(col - 1)){
          int remove = editMatrix[row - 1][col] + 1;
          int swap = editMatrix[row][col - 1] + 1;
          int add = editMatrix[row - 1][col - 1] + 1;
          editMatrix[row][col] = Math.min(remove, Math.min(swap, add));
        } else{
          editMatrix[row][col] =  editMatrix[row - 1][col - 1];
        }
      }     
    }
    oldWord = w2;

    return editMatrix[w2len][w1len]; 
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