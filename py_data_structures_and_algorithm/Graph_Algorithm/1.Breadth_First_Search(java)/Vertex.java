import java.util.List;
import java.util.ArrayList;

public class Vertex {
    
    private int data;
    private boolean visited;
    private List<Vertex> neighbourList;

    // On Vertex constructor it's going to get the data
    public Vertex(int data) {
        this.data = data;
        // instantiate neighbour to avoid null-pointer exception
        this.neighbourList = new ArrayList<>();
    }

    // Method addNeighbour
    public void addNeighbour(Vertex vertex) {
        this.neighbourList.add(vertex);
    }

    // Generate Getter and Setters for data, visited, and neighbour list.
    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }

    public boolean isVisited() {
        return visited;
    }

    public void setVisited(boolean visited) {
        this.visited = visited;
    }

    public List<Vertex> getNeighbourList() {
        return neighbourList;
    }

    public void setNeighbourList(List<Vertex> neighbourList) {
        this.neighbourList = neighbourList;
    }

    // The essence of the override is to get readable data when testing.
    @Override
    public String toString() {
        return ""+this.data;
    }
}