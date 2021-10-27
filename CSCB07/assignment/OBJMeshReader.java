package assignment;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;

public class OBJMeshReader implements MeshReader{

  @Override
  public HashSet<Polygon> read(String fileName) {
    HashSet<Polygon> polygons = new HashSet<Polygon>();
    
    try {
      
      File file = new File(fileName);
      BufferedReader reader = new BufferedReader(new FileReader(file));
      
      List<Vertex> allVertices = new ArrayList<Vertex>();
      
      String line;
      String data[];
      
      while((line = reader.readLine()) != null) {
        data = line.split(" ");

        if (data[0].equals("v")) {
         
          allVertices.add(new Vertex(
              Double.parseDouble(data[1]),
              Double.parseDouble(data[2]),
              Double.parseDouble(data[3])));
        }
        
        else {
          LinkedHashSet<Vertex> vertices = new LinkedHashSet<Vertex>();
          
          vertices.add(allVertices.get(Integer.parseInt(data[1])-1));
          vertices.add(allVertices.get(Integer.parseInt(data[2])-1));
          vertices.add(allVertices.get(Integer.parseInt(data[3])-1));
          
          polygons.add(new Polygon(vertices));
        }
      }
      
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }
    return polygons;
  }

}
