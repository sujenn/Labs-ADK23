package Lab3;
import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Exempel på in- och utdatahantering för maxflödeslabben i kursen
 * ADK.
 *
 * Använder Kattio.java för in- och utläsning.
 * Se http://kattis.csc.kth.se/doc/javaio
 *
 * @author: Per Austrin
 */

public class BipRed2 {
    Kattio io;
	int x;
	int y;
	int e;
	int[][] edges;
	int[][] flowEdges;
	int[][] flowSolution;
	int totflow;
	int v;
	int s;
	int t;

	int[][] c;  // kapacitet
    int[][] f;  // flöde
    int[][] cf; // restkapacitet
    int[] path; // augmenting path

	ArrayList<LinkedList<Integer>> neighbours;
    
    void readBipartiteGraph() {
		// Läs antal hörn och kanter
		x = io.getInt();
		y = io.getInt();
		e = io.getInt();
		
		// Läs in kanterna
		edges = new int[e][2];
		for (int i = 0; i < e; ++i) {
			edges[i][0] = io.getInt();
			edges[i][1] = io.getInt();
		}
    }
    
    void writeFlowGraph() {
		v = x + y + 2; 
		e = e + x + y;
		s = v - 1;
		t = v;
		
		// Debugutskrift
		System.err.println("Skickade iväg flödesgrafen");
    }

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
        s = s - 1;
        t = t - 1;

        f = new int[v][v];
        c = new int[v][v]; 
        cf = new int[v][v]; 
        flowEdges = new int[e][2];
        neighbours = new ArrayList<LinkedList<Integer>>();

        for (int i = 0; i < v; i++) {
            neighbours.add(new LinkedList<Integer>());
        }

		for (int i = 0; i < x; ++i) {
			int a = i;
			// Kant från s till a med kapacitet c
			flowEdges[i][0] = s;       
            flowEdges[i][1] = a;      
            c[s][a] = 1; 

            f[s][a] = 0;        	// f[u,v] = 0
            f[a][s] = 0;        	// f[v,u] = 0
            cf[s][a] = c[s][a];     // cf[u,v] = c[u,v]
            cf[a][s] = c[a][s]; 	// cf[v,u] = c[v,u]

            neighbours.get(s).add(a);
            neighbours.get(a).add(s);
		}
		for (int i = x; i < e - y; ++i) {
			int a = edges[i - x][0] , b = edges[i - x][1] ;
			// Kant från a till b med kapacitet c
			flowEdges[i][0] = a;       
            flowEdges[i][1] = b;      
            c[a][b] = 1; 

            f[a][b] = 0;        // f[u,v] = 0
            f[b][a] = 0;        // f[v,u] = 0
            cf[a][b] = c[a][b];     // cf[u,v] = c[u,v]
            cf[b][a] = c[b][a]; // cf[v,u] = c[v,u]

            neighbours.get(a).add(b);
            neighbours.get(b).add(a);
		}
		for (int i = e - y; i < e; ++i) {
			int b = x + i - (e - y);
			// Kant från b till t med kapacitet c
			flowEdges[i][0] = b;       
            flowEdges[i][1] = t;      
            c[b][t] = 1; 

            f[b][t] = 0;        	// f[u,v] = 0
            f[t][b] = 0;        	// f[v,u] = 0
            cf[b][t] = c[b][t];     // cf[u,v] = c[u,v]
            cf[t][b] = c[t][b]; 	// cf[v,u] = c[v,u]

            neighbours.get(b).add(t);
            neighbours.get(t).add(b);
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
		totflow = maxFlow;
		/*s++;
		t++;*/

		/*for (int i = 0; i < e; i++) {
            if (f[flowEdges[i][0]][flowEdges[i][1]] > 0) {
                flowEdges[i][0]++;
				flowEdges[i][1]++;
            }
        }*/

    }
    
    
    void readMaxFlowSolution() {
		// Läs in antal hörn, kanter, källa, sänka, och totalt flöde
		// (Antal hörn, källa och sänka borde vara samma som vi i grafen vi
		// skickade iväg)

		flowSolution = new int[totflow][3];	

		int j = 0;
		for (int i = 0; i < e; ++i) {
			// Flöde f från a till b
			if (f[flowEdges[i][0]][flowEdges[i][1]] > 0) {
				int a = flowEdges[i][0];
				int b = flowEdges[i][1];
				int flowf = f[flowEdges[i][0]][flowEdges[i][1]];
				if (!(a == s || b == t)) {
					flowSolution[j][0] = a;
					flowSolution[j][1] = b;
					flowSolution[j][2] = flowf;
					j++;
				}
			}
		}
		totflow = j;	//antalet kanter som har flow mellan sig mellan x och y hörnen
    }
    
    
    void writeBipMatchSolution() {
		int maxMatch = totflow;
		
		// Skriv ut antal hörn och storleken på matchningen
		io.println(x + " " + y);
		io.println(maxMatch);
		
		for (int i = 0; i < totflow; ++i) {
			int a = flowSolution[i][0], b = flowSolution[i][1];
			// Kant mellan a och b ingår i vår matchningslösning (har flöde 1)
			io.println(a + " " + b);
		}
	
    }
    
    BipRed2() {
		io = new Kattio(System.in, System.out);
		
		readBipartiteGraph();
		
		writeFlowGraph();

		fordFulkersonAlg();
		
		readMaxFlowSolution();
		
		writeBipMatchSolution();

		// debugutskrift
		System.err.println("Bipred avslutar\n");

		// Kom ihåg att stänga ner Kattio-klassen
		io.close();
    }
    
    public static void main(String args[]) {
		new BipRed2();
	
    }
}


