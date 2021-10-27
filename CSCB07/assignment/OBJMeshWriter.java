package assignment;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class OBJMeshWriter implements MeshWriter {

  @Override
  public void write(String fileName, HashSet<Polygon> polygons) {
    File file = new File(fileName);
    
    try {
      BufferedWriter writer = new BufferedWriter(new FileWriter(file));
      
      List<Vertex> allVertices = new ArrayList<Vertex>();
      
      String vertices = "";
      String faces = "";
      
      for (Polygon p: polygons) {
        faces += "f";
        for (Vertex v: p.vertices) {
          
          if (!allVertices.contains(v)) {
            allVertices.add(v);
            vertices += "v " + v.toString() + "\n";
          }
          
          faces += " " + (allVertices.indexOf(v)+1);
        }
        faces += "\n";
      }
//      for (Polygon p: polygons) {
//        faces += "f";
//        for (Vertex v: p.vertices) {
//          faces += " " + (allVertices.indexOf(v)+1);
//        }
//        faces += "\n";
//      }
//      

      writer.write((vertices + faces).trim());
      
      writer.close();
      
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }  
    
  }

}
