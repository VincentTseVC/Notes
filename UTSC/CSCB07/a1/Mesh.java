package assignment;

import java.util.HashSet;

public class Mesh extends GraphicalObject {
  HashSet<Polygon> polygons;
  MeshReader reader;
  MeshWriter writer;
  
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
//    for (Polygon p: polygons) 
//      p.transform(R);
    
    
    HashSet<Vertex> rotated = new HashSet<Vertex>();
    
    for (Polygon p: polygons) {
      for (Vertex v: p.vertices) {
        
        if (!rotated.contains(v)) {
          v.transform(R);
          rotated.add(v);
        }
      }
    }
  }
  
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
  
  public int hasCode() {
    // TODO: do it yourself
    return 1;
  }
  
  

}
