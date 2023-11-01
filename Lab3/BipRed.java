/**
 * Exempel på in- och utdatahantering för maxflödeslabben i kursen
 * ADK.
 *
 * Använder Kattio.java för in- och utläsning.
 * Se http://kattis.csc.kth.se/doc/javaio
 *
 * @author: Per Austrin
 */

public class BipRed {
    Kattio io;
	int x;
	int y;
	int e;
	int[][] edges;
	int[][] flowSolution;
	int totflow;
    
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
		int v = x + y, e2 = e + x + y, s = v + 1, t = v + 2;
		
		// Skriv ut antal hörn och kanter samt källa och sänka
		io.println(v + 2);
		io.println(s + " " + t);
		io.println(e2);
		int c = 1;
		for (int i = 0; i < x; ++i) {
			int a = i + 1;
			// Kant från s till a med kapacitet c
			io.println(s + " " + a + " " + c);
		}
		for (int i = 0; i < e; ++i) {
			int a = edges[i][0], b = edges[i][1];
			// Kant från a till b med kapacitet c
			io.println(a + " " + b + " " + c);
		}
		for (int i = 0; i < y; ++i) {
			int b = x + i + 1;
			// Kant från b till t med kapacitet c
			io.println(b + " " + t + " " + c);
		}
		// Var noggrann med att flusha utdata när flödesgrafen skrivits ut!
		io.flush();
		
		// Debugutskrift
		System.err.println("Skickade iväg flödesgrafen");
    }
    
    
    void readMaxFlowSolution() {
		// Läs in antal hörn, kanter, källa, sänka, och totalt flöde
		// (Antal hörn, källa och sänka borde vara samma som vi i grafen vi
		// skickade iväg)
		
		int v = io.getInt();
		int s = io.getInt();
		int t = io.getInt();
		totflow = io.getInt();
		int e = io.getInt();

		flowSolution = new int[totflow][3];	
		
		int j = 0;
		for (int i = 0; i < e; ++i) {
			// Flöde f från a till b
			int a = io.getInt();
			int b = io.getInt();
			int f = io.getInt();
			if (!(a == s || b == t)) {
				flowSolution[j][0] = a;
				flowSolution[j][1] = b;
				flowSolution[j][2] = f;
				j++;
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
    
    BipRed() {
		io = new Kattio(System.in, System.out);
		
		readBipartiteGraph();
		
		writeFlowGraph();
		
		readMaxFlowSolution();
		
		writeBipMatchSolution();

		// debugutskrift
		System.err.println("Bipred avslutar\n");

		// Kom ihåg att stänga ner Kattio-klassen
		io.close();
    }
    
    public static void main(String args[]) {
		new BipRed();
	
    }
}

