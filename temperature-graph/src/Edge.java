import java.util.ArrayList;

/**
 * Created by sherrysarkar on 10/15/17.
 * TODO: Hashcodes?
 */
public class Edge {
    private Node start;
    private Node end;
    private ArrayList<String> employees;
    private int weight;

    public Edge(Node s, Node e, ArrayList<String> em, int w) {
        start = s;
        end = e;
        employees = em;
        weight = w;

        // When an edge is created, the nodes are updated.
        start.edges.add(this);
        end.edges.add(this);
    }

    public Edge(Node s, Node e, int w) {
        this(s, e, null, w);
    }

    public Node getStart(){
        return start;
    }

    public Node getEnd() { return end; }

    public ArrayList<String> getEmployees() {
        return employees;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Edge) {
            Edge e = (Edge) obj;
            Node st = e.getStart();
            Node en = e.getEnd();

            return start.equals(st) && end.equals(en);
        }
        return false;
    }
}
