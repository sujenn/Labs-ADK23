package Lab3;
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
    
    int[][] readBipartiteGraph() {
		// Läs antal hörn och kanter
		
		int x = io.getInt();
		int y = io.getInt();
		int e = io.getInt();
		
		// Läs in kanterna
		int[][] all = new int[e + 2][2];
		all[0][0] = x;
		all[0][1] = y;
		all[1][0] = e;
		for (int i = 0; i < e; ++i) {
			int a = io.getInt();
			int b = io.getInt();
			all[i + 2][0] = a;
			all[i + 2][1] = b;
		}
		return all;
    }
    
    
    void writeFlowGraph(int[][] elements) {
		int v = elements[0][0] + elements[0][1], e = elements[1][0], s = v + 1, t = v + 2;
		
		// Skriv ut antal hörn och kanter samt källa och sänka
		io.println(v);
		io.println(s + " " + t);
		io.println(e);
		for (int i = 0; i < e; ++i) {
			int a = elements[i + 2][0], b = elements[i + 2][1], c = 1;
			// Kant från a till b med kapacitet c
			io.println(a + " " + b + " " + c);
		}
		// Var noggrann med att flusha utdata när flödesgrafen skrivits ut!
		io.flush();
		
		// Debugutskrift
		System.err.println("Skickade iväg flödesgrafen");
    }
    
    
    int[][] readMaxFlowSolution() {
		// Läs in antal hörn, kanter, källa, sänka, och totalt flöde
		// (Antal hörn, källa och sänka borde vara samma som vi i grafen vi
		// skickade iväg)
		
		int v = io.getInt();
		int s = io.getInt();
		int t = io.getInt();
		int totflow = io.getInt();
		int e = io.getInt();

		int[][] flowSolution = new int[e + 3][3];
		flowSolution[0][0] = v;
		flowSolution[1][0] = s;
		flowSolution[1][1] = t;
		flowSolution[1][2] = totflow;
		flowSolution[2][0] = e;



		for (int i = 0; i < e; ++i) {
			// Flöde f från a till b
			int a = io.getInt();
			int b = io.getInt();
			int f = io.getInt();
			flowSolution[i + 3][0] = a;
			flowSolution[i + 3][1] = b;
			flowSolution[i + 3][2] = f;
		}
		return flowSolution;
    }
    
    
    void writeBipMatchSolution(int[][] flowSolution) {
		int x = flowSolution[][], y = io.getInt(), maxMatch = flowSolution[1][2];
		
		// Skriv ut antal hörn och storleken på matchningen
		io.println(x + " " + y);
		io.println(maxMatch);
		
		for (int i = 0; i < maxMatch; ++i) {
			int a = io.getInt(), b = io.getInt();
			// Kant mellan a och b ingår i vår matchningslösning
			io.println(a + " " + b);
		}
	
    }
    
    BipRed() {
		io = new Kattio(System.in, System.out);
		
		int[][] elements = readBipartiteGraph();
		
		writeFlowGraph(elements);
		
		int[][] flowSolution = readMaxFlowSolution();
		
		writeBipMatchSolution(flowSolution);

		// debugutskrift
		System.err.println("Bipred avslutar\n");

		// Kom ihåg att stänga ner Kattio-klassen
		io.close();
    }
    
    public static void main(String args[]) {
		new BipRed();
	
    }
}

