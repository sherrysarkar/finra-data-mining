import java.util.HashSet;

/**
 * Created by sherrysarkar on 10/15/17.
 * TODO: Hashcodes?
 */
public class Node {
    private String companyName;
    private int temperature;

    public Node (String name, int temp) {
        companyName = name;
        temperature = temp;
    }

    public Node (String name) {
        this(name, 0);
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

    public void incrementTemperature(int t) {
        temperature += t;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Node) {
            Node n = (Node) obj;
            return companyName.equals(n.getCompanyName());
        }
        return false;
    }

    @Override
    public int hashCode() {
        return companyName.hashCode();
    }
}
