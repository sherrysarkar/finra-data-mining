import java.util.ArrayList;

/**
 * Created by sherrysarkar on 10/15/17.
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
}
