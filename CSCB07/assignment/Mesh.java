package assignment;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Mesh extends GraphicalObject {
  HashSet<Polygon> polygons;
  private MeshReader reader;
  private MeshWriter writer;
  
  public void setReader(MeshReader reader) {
    this.reader = reader;
  }
  
  public void setWriter(MeshWriter writer) {
    this.writer = writer;
  }
  
  public void readFromFile(String fileName) {
    polygons = reader.read(fileName);
  }
  
  public void writeToFile(String fileName) {
    writer.write(fileName, polygons);
  }

  @Override
  public void transform(double[][] R) {
    System.out.println("tranforming Mesh");
    List<Vertex> rotated = new ArrayList<Vertex>();
    for (Polygon p: polygons) {
      
      for (Vertex v: p.vertices) {
        if (!rotated.contains(v)) {
          v.transform(R);
          rotated.add(v);
        }
      }
//      
//      System.out.println(p);
//      p.transform(R);
    }
  }
  
  @Override
  public boolean equals(Object o) {
    
    if (o == null)
      return false;
    
    if (o == this) 
      return true;
    
    if (!(o instanceof Mesh)) 
      return false;
    
    Mesh other = (Mesh) o;
    
    return this.polygons.equals(other.polygons);
  }
  
  @Override
  public int hashCode() {
    // TODO: 
    return 0;
  }
  
  
  
}
