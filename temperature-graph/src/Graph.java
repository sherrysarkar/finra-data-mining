import java.util.HashMap;
import java.util.Collection;
/**
 * Created by sherrysarkar on 10/15/17.
 * TODO: Hashcodes?
 */
public class Graph {
    private HashMap<Node, HashMap<Node, Edge>> graph = new HashMap();

    public Graph(Collection<String> names) {
        for (String name : names) {
            graph.put(new Node(name), new HashMap<Node, Edge>());
        }
    }

    public HashMap<Node, HashMap<Node, Edge>> getGraph() {
        return graph;
    }
}
