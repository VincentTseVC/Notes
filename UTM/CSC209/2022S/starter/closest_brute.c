#include <math.h>

#include "closest_brute.h"

double brute_force(struct Point P[], size_t n) 
{ 
    if (n == 1) return 0.0;

    // double min_dist = dist(P[0], P[1]);
    double min_dist = INFINITY;
    double curr_dist;

    for (int i = 0; i < n-1; i++){
        for (int j = i+1; j < n; j++){
            curr_dist = dist(P[i], P[j]);
            if (min_dist > curr_dist){
                min_dist = curr_dist;
            }
        }
    }

    return min_dist;
} 
