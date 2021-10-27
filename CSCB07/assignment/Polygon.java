package assignment;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;

public class Polygon extends GraphicalObject {
  LinkedHashSet<Vertex> vertices;
  
  public Polygon(LinkedHashSet<Vertex> vertices) {
    this.vertices = vertices;
  }

  @Override
  public void transform(double[][] R) {
    System.out.println("tranforming Polygon");
    List<Vertex> rotated = new ArrayList<Vertex>();
    
    for (Vertex v: vertices) {
      if (!rotated.contains(v)) {
        v.transform(R);
        rotated.add(v);
      }
    }
  }
  
  @Override
  public boolean equals(Object o) {
    
    if (o == null)
      return false;
    
    if (o == this) 
      return true;
    
    if (!(o instanceof Polygon)) 
      return false;
    
    Polygon other = (Polygon) o;
    
    return this.vertices.equals(other.vertices);
  }
  
  @Override
  public int hashCode() {
    // TODO: 
    return 0;
  }
  
  
  
  
  
}
