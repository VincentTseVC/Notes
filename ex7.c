/**
 * Exercise 7 - Convolutions and Edge detection!
 *
 * Please read the comments below carefully, they describe your task in detail.
 * Any clarifications and corrections will be posted to Piazza so please keep
 * an eye on the forum!
 *
 * Starter code:  Mustafa Quraish, 2020
 */

#include "imgUtils.c"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Image dimensions
#define SIZEX 512
#define SIZEY 512

// Kernel size
#define K_SIZE 3

// Declaration of the X and Y kernel matrices.
double GX[K_SIZE][K_SIZE] = {
    {1, 0, -1},
    {2, 0, -2},
    {1, 0, -1},
};

double GY[K_SIZE][K_SIZE] = {
    {1, 2, 1},
    {0, 0, 0},
    {-1, -2, -1},
};

/*****************************************************************************/

double convolve(unsigned char inp[SIZEY][SIZEX], int px, int py,
                double kernel[K_SIZE][K_SIZE])
{
  /**
   * Perform the convolution of the given kernel and the image with (px, py) as
   * the center pixel. In essense, the center of the kernel is placed at the
   * given pixel, and you compute weighted sum (refer to tha handout for an
   * example) and return it.
   *
   * If (px, py) is one of the pixels at the edge of the screen (and thus part
   * of the kernel is leaking outside the image), you may assume that those
   * pixels are black. In other words, you should pretend that all pixels
   * outside the image are just black for the sake of computation.
   *
   * Note: In this case, the weighted sum is also an integer because of GX and
   *       GY. However, in general the kernels can have floating point values,
   *       so doing it this way will let you generalize your solution much more
   *       easily if you wish to do so.
   */

  // all the directions
  int result = 0;

  int row_nbr[] = {-1, -1, -1,  0, 0,  1, 1, 1};
  int col_nbr[] = {-1,  0,  1, -1, 1, -1, 0, 1};

  int new_x, new_y;
  for (int i = 0; i < 8; i++) {
    new_y = py + row_nbr[i];  // new row
    new_x = px + col_nbr[i];  // new col

    // if new_x or new_y is outside of the image range, skip (do nothing)
    // if (new_x < 0 || new_x >= SIZEX || new_y < 0 || new_y >= SIZEY) continue;

    if (new_x < 0 || new_x >= SIZEX || new_y < 0 || new_y >= SIZEY) 
      result += 0;
    else
      result += inp[new_y][new_x] * kernel[1 + row_nbr[i]][1 + col_nbr[i]];  // (1, 1) is the center of the grid
    
  }

  return result;

}

void sobel(unsigned char inp[SIZEY][SIZEX], unsigned char out[SIZEY][SIZEX])
{
  /**
   * Given an input image, perform the Sobel edge detection algorithm and store
   * the output in `out`.  Remember that this boils down to:
   *
   * for pixel in input:
   *    g_x = convolve GX at pixel
   *    g_y = convolve GY at pixel
   *    set corresponding output pixel to sqrt(g_x^2 + g_y^2)
   *
   * Note: The expression sqrt(g_x^2 + g_y^2) may result in values greater than
   *       255. If the value is greater, just set it equal to 255. Round down
   *       in case of floating point values.
   * 
   * (x, y) => (1, 2) => a[2][1]
   */

  double g_x, g_y, pixel;

  for (int py = 0; py < SIZEY; py++) {  // row
    for (int px = 0; px < SIZEX; px++) {  // col

      // apply the formula, get px and py
      g_x = convolve(inp, px, py, GX);
      g_y = convolve(inp, px, py, GY);
      // get the result colour of sqrt(g_x^2 + g_y^2)
      pixel = sqrt(g_x * g_x + g_y * g_y);

      // if colour is > 255, make the the whitest color
      if (pixel > 255) pixel = 255;

      // set the color in the out image
      out[py][px] = pixel;
    }
  }
}

/*****************************************************************************/

#ifndef __testing__ // You know the drill, don't remove this

int main()
{
  /* Feel free to change the contents INSIDE the main function to help test */

  // Initialize the 2D-arrays that will store the values of the pixels
  unsigned char data[SIZEY][SIZEX];
  unsigned char edge[SIZEY][SIZEX];

  // We will store the values of the input image
  readPGM("input.pgm", &data[0][0]);

  // Test convolve()
  double res = convolve(data, 0, 0, GY);
  if (res != -132.0)
  {
    printf("Error: convolve() test 1 output incorrect.\n");
    printf("Expected: %f,  Yours: %f\n", -132.0, res);
    exit(1);
  }

  // Pixel somewhere in the middle
  res = convolve(data, 324, 218, GX);
  if (res != -21.0)
  {
    printf("Error: convolve() test 2 output incorrect.\n");
    printf("Expected: %f,  Yours: %f\n", -21.0, res);
    exit(1);
  }

  printf("- convolve() output was correct.\n");

  // Call the sobel function
  sobel(data, edge);

  // Write the values to the output image
  writePGM("output.pgm", &edge[0][0]);

  // Compare to the expected image
  readPGM("expected.pgm", &data[0][0]);

  for (int i = 0; i < SIZEX; i++)
  {
    for (int j = 0; j < SIZEY; j++)
    {
      if (data[j][i] != edge[j][i])
      {
        printf("Error: Pixel (x=%d, y=%d) has the wrong colour.\n", i, j);
        printf("Expected: %u,  Yours: %u\n", data[j][i], edge[j][i]);
        exit(1);
      }
    }
  }

  printf("- sobel() output was correct.\n");
  return 0;
}

#endif
