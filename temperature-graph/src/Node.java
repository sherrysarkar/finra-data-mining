import java.util.List;

/**
 * Created by sherrysarkar on 10/15/17.
 */
public class Node {
    private String companyName;
    public List<Edge> edges;
    private int temperature;

    public Node (String name, List<Edge> e, int temp) {
        companyName = name;
        edges = e;
        temperature = temp;
    }

    public Node (String name, List<Edge> e) {
        this(name, e, 0);
    }

    public String getCompanyName() {
        return companyName;
    }

    public List<Edge> getEdges() {
        return edges;
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int t) {
        temperature = t;
    }


}
