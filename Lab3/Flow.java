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
    ArrayList<LinkedList<Integer>> neighbours;

    boolean bfs() {
        boolean visited[] = new boolean[v];

        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.add(s);
        visited[s] = true;
        path[s] = -1;

        while (queue.size() != 0) { 
            int x = queue.poll();

            LinkedList<Integer> node = neighbours.get(x);
            for (int i = 0; i < node.size(); i++) {
                if (visited[node.get(i)] == false && cf[x][node.get(i)] > 0) {
                    if (node.get(i) == t) {
                        path[node.get(i)] = x;
                        return true;
                    }
                    queue.add(node.get(i));
                    path[node.get(i)] = x;
                    visited[node.get(i)] = true;
                }
            
            }
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
        neighbours = new ArrayList<LinkedList<Integer>>();

        for (int i = 0; i < v; i++) {
            neighbours.add(new LinkedList<Integer>());
        }

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

            neighbours.get(a).add(b);
            neighbours.get(b).add(a);
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

