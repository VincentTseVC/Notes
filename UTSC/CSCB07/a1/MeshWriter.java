package assignment;

import java.util.HashSet;

public interface MeshWriter {
  public void write(String fileName, HashSet<Polygon> polygons);
}
