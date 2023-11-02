import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.HashMap;

/**
 * Exempel på in- och utdatahantering för maxflödeslabben i kursen
 * ADK.
 *
 * Använder Kattio.java för in- och utläsning.
 * Se http://kattis.csc.kth.se/doc/javaio
 *
 * @author: Per Austrin
 */

public class BipRed3 {
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

	//int[][] c;  // kapacitet
    //int[][] f;  // flöde
    //int[][] cf; // restkapacitet
    int[] path; // augmenting path

    HashMap<Integer, Integer> c;
    HashMap<Integer, Integer> f;
    HashMap<Integer, Integer> cf;

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
                if (visited[node.get(i)] == false && cf.get(x*10000 + node.get(i)) > 0) {
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

        //10000*u + v
        //111110000

        c = new HashMap<Integer, Integer>();
        f = new HashMap<Integer, Integer>();
        cf = new HashMap<Integer, Integer>();


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
            
            int key1 = s*10000 + a;
            int key2 = a*10000 + s;
            
            c.put(key1, 1);    
            f.put(key1, 0); 
            f.put(key2, 0); 
            cf.put(key1, 1); 
            cf.put(key2, 0);
            //cf.put(key1, c.get(key1)); 
            //cf.put(key2, c.get(key2));

            /*f[s][a] = 0;        	// f[u,v] = 0
            f[a][s] = 0;        	// f[v,u] = 0
            cf[s][a] = c[s][a];     // cf[u,v] = c[u,v]
            cf[a][s] = c[a][s]; 	// cf[v,u] = c[v,u]*/

            neighbours.get(s).add(a);
            neighbours.get(a).add(s);
		}
		for (int i = x; i < e - y; ++i) {
			int a = edges[i - x][0] - 1, b = edges[i - x][1] - 1; //första felet pga index lmao
			// Kant från a till b med kapacitet c
			flowEdges[i][0] = a;       
            flowEdges[i][1] = b;  

            int key1 = a*10000 + b;
            int key2 = b*10000 + a;  

            c.put(key1, 1); 
            f.put(key1, 0); 
            f.put(key2, 0); 
            cf.put(key1, 1); 
            cf.put(key2, 0);

            neighbours.get(a).add(b);
            neighbours.get(b).add(a);
		}
		for (int i = e - y; i < e; ++i) {
			int b = x + i - (e - y);
			// Kant från b till t med kapacitet c
			flowEdges[i][0] = b;       
            flowEdges[i][1] = t;  
            
            int key1 = b*10000 + t;
            int key2 = t*10000 + b; 

            c.put(key1, 1); 
            f.put(key1, 0); 
            f.put(key2, 0); 
            cf.put(key1, 1); 
            cf.put(key2, 0); 

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
                //r = Math.min(cf[a][b], r);
                r = Math.min(cf.get(a*10000 + b), r);
                b = a;
            }

            b = t;
            while (b != s) {
                int a = path[b];
                //f[a][b] += r;
                f.put(a*10000 + b, f.get(a*10000 + b) + r);
                //f[b][a] = -f[a][b];
                f.put(b*10000 + a, -f.get(a*10000 + b));
                //cf[a][b] = c[a][b] - f[a][b];
                Integer newC = c.get(a*10000 + b);
                if (newC == null) {
                    newC = 0;
                }
                Integer newC2 = c.get(b*10000 + a);
                if (newC2 == null) {
                    newC2 = 0;
                }
                cf.put(a*10000 + b, newC - f.get(a*10000 + b));
                //cf[b][a] = c[b][a] - f[b][a];
                cf.put(b*10000 + a, newC2 - f.get(b*10000 + a));

                b = a;
            }
            maxFlow += r;
        }
		totflow = maxFlow;
    }
    
    void readMaxFlowSolution() {
		// Läs in antal hörn, kanter, källa, sänka, och totalt flöde
		// (Antal hörn, källa och sänka borde vara samma som vi i grafen vi
		// skickade iväg)

		flowSolution = new int[totflow][3];	

		int j = 0;
		for (int i = 0; i < e; ++i) {
			// Flöde f från a till b
			if (f.get(flowEdges[i][0]*10000 + flowEdges[i][1]) > 0) {
				int a = flowEdges[i][0];
				int b = flowEdges[i][1];
				int flowf = f.get(flowEdges[i][0]*10000 + flowEdges[i][1]);
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
			int a = flowSolution[i][0] + 1, b = flowSolution[i][1] + 1;  //andra felet pga index
			// Kant mellan a och b ingår i vår matchningslösning (har flöde 1)
			io.println(a + " " + b);
		}
        io.flush();
	
    }
    
    BipRed3() {
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
		new BipRed3();
	
    }
}


