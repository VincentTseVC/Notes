#include "closest_helpers.h"

#include <math.h>

int verbose = 0;

int compare_x(const void* a, const void* b) 
{
    // return ((struct Point *) a)->x - ((struct Point *) a)->x;
    const struct Point *a_ = a;
    const struct Point *b_ = b;
    return a_->x - b_->x;
} 

int compare_y(const void* a, const void* b) 
{ 
    const struct Point *a_ = a;
    const struct Point *b_ = b;
    return a_->y - b_->y;
} 

double dist(struct Point p1, struct Point p2) 
{
    long int x = pow(p1.x-p2.x, 2);
    long int y = pow(p1.y-p2.y, 2);
    return sqrt(x + y);
} 
