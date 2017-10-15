import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by sherrysarkar on 10/15/17.
 */
public class Construction {

    public Construction() {

    }

    /**
     * TODO: Extract list of bad people -> company from CSV and put in dictionary.
     */

    HashMap<String, String> badPerson_to_Company = new HashMap<>();

    /**
     * TODO: Extract list of person -> employment history and put in dictionary.
     */

    HashMap<String, String[]> person_to_history = new HashMap<>();

    /**
     * Constructs graph based on extracted data.
     * @return Fully constructed graph
     */
    public Graph constructGraph() {
        Graph g = new Graph(new HashSet<Node>());
        Set<String> badSet = badPerson_to_Company.keySet();

        for (String bad_person : badSet) {
            String[] employ_history = person_to_history.get(bad_person);
            if (employ_history.length > 1) {

                // Starts at 1 so that you can look to the company before you as the "before node".
                for (int i = 1; i < employ_history.length; i++) {
                    Node before = new Node(employ_history[i - 1]);
                    Node after = new Node(employ_history[i]);

                    /**
                     * TODO: Check if nodes exist yet; if they do exist, retrieve them and make them before / after.
                     * TODO: After you've made a new node, make sure to add it to Graph object.
                     */

                    Edge person = new Edge(before, after, 0); // INCORRECT!!!!! makes a new edge, and updates nodes

                    // Checking if this edge exists yet
                    if (before.edges.contains(person)) {
                        /**
                         * TODO: Retrieve edge, and update weight.
                          */
                    }
                }
            }
        }

        return null;
    }

}
