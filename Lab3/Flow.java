package Lab3;
import java.util.LinkedList;
import java.util.Arrays; 
import java.util.ArrayList; 

public class Flow {
    Kattio io;
    int[][] c;  // kapacitet
    int[][] f;  // flöde
    int[][] cf; // restkapacitet
    int[] path; // augmenting path
    int s;
    int t;
    int v;
    int[][] edges;
    LinkedList<Integer>[] neighbours;
    //ArrayList<LinkedList<Integer>[]> neighbours;

    /* Funktionen bfs är tagen och anpassad från GeeksForGeeks */
    boolean bfs() {
        boolean visited[] = new boolean[v];
        //Arrays.fill(visited, false);    //all nodes start as nonvisited (false)

        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.add(s);
        visited[s] = true;
        path[s] = -1;

        while (queue.size() != 0) { 
            int x = queue.poll();

            for (int y = 0; y < v; y++) { // Går igenom alla andra noder och inte bara grannar (edges)
                if (visited[y] == false && cf[x][y] > 0) {
                    if (y == t) {
                        path[y] = x;
                        return true;
                    }
                    queue.add(y);
                    path[y] = x;
                    visited[y] = true;
                }
            }

            /*for (int i = 0; i < neighbours[x].size(); i++) {
                if (visited[neighbours[x].get(i)] == false && cf[x][neighbours[x].get(i)] > 0) {
                    if (neighbours[x].get(i) == t) {
                        path[neighbours[x].get(i)] = x;
                        return true;
                    }
                    queue.add(neighbours[x].get(i));
                    path[neighbours[x].get(i)] = x;
                    visited[neighbours[x].get(i)] = true;
                }
            
            }*/
        }
        return false;
    }

    void fordFulkersonAlg() {
        v = io.getInt();
        s = io.getInt()-1;
        t = io.getInt()-1;
        int e = io.getInt();

        f = new int[v][v];
        c = new int[v][v]; 
        cf = new int[v][v]; 
        edges = new int[e][2];
        //neighbours = new ArrayList<>(v);

        for (int i = 0; i < neighbours.length; i++) {
            neighbours[i] = new LinkedList<Integer>();
        }

        /*for (int i = 0; i < v; i++) {
            neighbours.add(new LinkedList<Integer>());
        }*/

        for (int i = 0; i < e; i++) {
            int a = io.getInt()-1;  // u in pseudocode 
            int b = io.getInt()-1;  // v in psuedocode
            int cap = io.getInt();
            edges[i][0] = a;       
            edges[i][1] = b;      
            c[a][b] = cap; 

            f[a][b] = 0;        // f[u,v] = 0
            f[b][a] = 0;        // f[v,u] = 0
            cf[a][b] = cap;     // cf[u,v] = c[u,v]
            cf[b][a] = c[b][a]; // cf[v,u] = c[v,u]

            neighbours[a].add(b);
            neighbours[b].add(a);
        }

        int maxFlow = 0;

        path = new int[v]; 

        while(bfs()) {
            int r = Integer.MAX_VALUE;      // a = u
            int b = t;                      // b = v
            while (b != s) {
                int a = path[b];
                r = Math.min(cf[a][b], r);
                b = a;
            }

            b = t;
            while (b != s) {
                int a = path[b];
                f[a][b] += r;
                f[b][a] = -f[a][b];
                cf[a][b] = c[a][b] - f[a][b];
                cf[b][a] = c[b][a] - f[b][a];
                b = a;
            }
            maxFlow += r;
        }

        io.println(v);
        io.println((s+1) + " " + (t+1) + " " + maxFlow);

        int countPos = 0;
        for (int i = 0; i < e; i++) {
            if (f[edges[i][0]][edges[i][1]] > 0) {
                countPos++;
            }
        }

        io.println(countPos);

        for (int i = 0; i < e; i++) {
            if (f[edges[i][0]][edges[i][1]] > 0) {
                io.println((edges[i][0]+1) + " " + (edges[i][1]+1) + " " + f[edges[i][0]][edges[i][1]]);

            }
        }
    }

    Flow() {
        io = new Kattio(System.in, System.out);

        fordFulkersonAlg();

        io.close();
    }

    public static void main(String args[]) {
		new Flow();
	
    }
}

