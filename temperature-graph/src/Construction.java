import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.io.PrintStream;

/**
 * Created by sherrysarkar on 10/15/17.
 */
public class Construction {


    /**
     * TODO: Extract list of bad people -> company from CSV and put in dictionary.
     */

    static HashMap<String, String> badPerson_to_Company = new HashMap<>();

    /**
     * TODO: Extract list of person -> employment history and put in dictionary.
     */

    static HashMap<String, ArrayList<String>> person_to_history = new HashMap<>();

    /**
     * Constructs graph based on extracted data.
     * @return Fully constructed graph
     */
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scan = new Scanner(new File("../../data/FINALCASELINKS.txt"));
        while(scan.hasNextLine()) {
            String line = scan.nextLine();
            line = line.replaceAll("\\s+", "");
            String[] words = line.split(",");
            badPerson_to_Company.put(words[1], words[2]);
        }
        scan.close();
        scan = new Scanner(new File("peopleObjects.csv"));
        while(scan.hasNextLine()) {
            String line = scan.nextLine();
            line = line.replaceAll("\\s+", "");
            String[] words = line.split(",");
            ArrayList<String> list = new ArrayList<>();
            for (int i = 1; i < words.length; i++) {
                list.add(words[i]);
            }
            person_to_history.put(words[0], list);
        }
        scan.close();

        HashSet<String> companies = new HashSet<>();
        Set<String> badSet = badPerson_to_Company.keySet();
        for (String key : badSet) {
            companies.add(badPerson_to_Company.get(key));
            companies.addAll(person_to_history.get(key));
        }
        Graph g = new Graph(companies);
        HashMap<Node, HashMap<Node, Edge>> adj = g.getGraph();
        for (String bad_person : badSet) {
            ArrayList<String> employ_history = person_to_history.get(bad_person);
            if (employ_history.size() > 1) { //This seems pointless rn???

                // Starts at 1 so that you can look to the company before you as the "before node".
                for (int i = 1; i < employ_history.size(); i++) {
                    Node before = new Node(employ_history.get(i - 1));
                    Node after = new Node(employ_history.get(i));
                    if (adj.get(before).containsKey(after)) {
                        adj.get(before).get(after).incrementWeight(1);
                    } else {
                        adj.get(before).put(after, new Edge(before, after, 1));
                    }
                }
            }
        }



        PrintStream stream = new PrintStream(new File("graph.csv"));
        stream.println(adj.keySet().size());
        for (Node key : adj.keySet()) {
            int sum = 0;
            stream.print(key.getCompanyName());
            for (Node edge : adj.get(key).keySet()) {
                sum += adj.get(key).get(edge).getWeight();
            }
            stream.print(",");
            stream.print(sum);
            stream.print(";");
        }

        stream.println();
        for (Node key : adj.keySet()) {
            stream.print(key.getCompanyName());
            for (Node edge : adj.get(key).keySet()) {
                stream.print(adj.get(key).get(edge).getStart().getCompanyName());
                stream.print(",");
                stream.print(adj.get(key).get(edge).getEnd().getCompanyName());
                stream.print(";");
            }
        }
        stream.close();
    }

}
