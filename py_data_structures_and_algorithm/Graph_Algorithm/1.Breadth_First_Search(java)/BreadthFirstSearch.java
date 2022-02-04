import java.util.Queue;
import java.util.LinkedList;

public class BreadthFirstSearch {

    // Method with starting vertex(root)
    public void bfs(Vertex root) {
        // Implement queue for the vertex (implemented with Linked List)
        Queue<Vertex> queue = new LinkedList<>();

        root.setVisited(true);
        queue.add(root);

        while (!queue.isEmpty()) {
            Vertex actualVertex = queue.remove();
            System.out.print(actualVertex+"-");

            for(Vertex v : actualVertex.getNeighbourList()) {
                if (!v.isVisited()) {
                    // set visted to true and to queue
                    v.setVisited(true);
                    queue.add(v);
                }
            }
        }
    }
}