package assignment;

import java.util.LinkedHashSet;

public class Polygon extends GraphicalObject {
  LinkedHashSet<Vertex> vertices;
  
  public Polygon(LinkedHashSet<Vertex> vertices) {
    this.vertices = vertices;
  }

  @Override
  public void transform(double[][] R) {
     for (Vertex v: vertices)
       v.transform(R);
    
//    LinkedHashSet<Vertex> rotated = new LinkedHashSet<Vertex>();
//    for (Vertex v: vertices) {
//      if (!rotated.contains(v)) {
//        v.transform(R);
//        rotated.add(v);
//      }
//    }
  }
  
  public boolean equals(Object o) {
    if (o == null)
      return false;
    
    if (o == this)
      return true;
    
    if (!(o instanceof Polygon))
      return false;
    
    Polygon other = (Polygon) o;
    
    // TODO: Ask Piazza, does order Matter?
    
    return this.vertices.equals(other.vertices);
  }
  
  public int hasCode() {
    // TODO:
    return 1;
  }
  
}
