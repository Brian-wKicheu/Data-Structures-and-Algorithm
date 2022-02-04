public class Test {
    
    public static void main(String[] args) {

        BreadthFirstSearch breadthfirstsearch = new BreadthFirstSearch();

        Vertex vertex1 = new Vertex(1);
        Vertex vertex2 = new Vertex(2);
        Vertex vertex3 = new Vertex(3);
        Vertex vertex4 = new Vertex(4);
        Vertex vertex5 = new Vertex(5);

        // Add neighbours
        vertex1.addNeighbour(vertex2); // left child
        vertex1.addNeighbour(vertex4); // right child
        vertex4.addNeighbour(vertex5);
        vertex2.addNeighbour(vertex3);
        /*      
                    1
                  /   \
                 2     4
                /       \
               3         5
        */
        // The root is 'vertex1'
        breadthfirstsearch.bfs(vertex1);
    }
}