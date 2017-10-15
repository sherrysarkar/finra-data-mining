import java.util.HashSet;

/**
 * Created by sherrysarkar on 10/15/17.
 */
public class Node {
    private String companyName;
    public HashSet<Edge> edges;
    private int temperature;

    public Node (String name, HashSet e, int temp) {
        companyName = name;
        edges = e;
        temperature = temp;
    }

    public Node (String name, HashSet<Edge> e) {
        this(name, e, 0);
    }

    public String getCompanyName() {
        return companyName;
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int t) {
        temperature = t;
    }

}
