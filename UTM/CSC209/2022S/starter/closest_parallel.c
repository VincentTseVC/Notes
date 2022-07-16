#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include "closest_parallel.h"


int curr_depth = 0;

double _closest_parallel(struct Point P[], size_t n, int pdmax, int *pcount)
{
    static int num_forks = 0;

    if (n <= 3 || pdmax <= 0) 
        return _closest_serial(P, n);
    
    int p_mid = n / 2;
    
    // === left child ===
    double dl;
    int fdl[2];
    if (pipe(fdl) == -1) {
        perror("pipe");
        exit(1);
    }

    pid_t pl;
    if ((pl = fork()) == -1) {
        perror("fork");
        exit(1);
    }
    // child
    if(pl == 0) {
        // child doesnt need read-end
        close(fdl[0]);

        double dl_temp = _closest_parallel(P, p_mid, pdmax-1, pcount);
        // write
        if (write(fdl[1], &dl_temp, sizeof(double)) == -1){
            perror("write to pipe");
            exit(1);
        }

        close(fdl[1]);
        num_forks += 1;
        exit(num_forks); // left child ends
    }

    // === right child ===
    double dr;
    int fdr[2];
    if (pipe(fdr) == -1) {
        perror("pipe");
        exit(1);
    }
    pid_t pr;
    if ((pr = fork()) == -1) {
        perror("fork");
        exit(1);
    }
    // child
    if(pr == 0) {
        // child doesnt need read-end
        close(fdl[0]);
        close(fdl[1]);
        close(fdr[0]);

        double dr_temp = _closest_parallel(P+p_mid, n-p_mid, pdmax-1, pcount);
        // write
        if (write(fdr[1], &dr_temp, sizeof(double)) == -1){
            perror("write to pipe");
            exit(1);
        }

        close(fdr[1]);
        num_forks += 1;
        exit(num_forks); // right child ends
    }


    // parent
    close(fdl[1]);
    close(fdr[1]);

    int status;
    pid_t p;
    for (int i = 0; i < 2; i++) {
        if ((p = wait(&status)) == -1) {
            perror("wait");
            exit(1);
        }   

        if (WIFEXITED(status)) {
            num_forks = WEXITSTATUS(status);

            if (p == pl) {
                if (read(fdl[0], &dl, sizeof(double)) == 0) {
                    perror("read");
                    exit(1);
                }
            } else {
                if (read(fdr[0], &dr, sizeof(double)) == 0) {
                    perror("read");
                    exit(1);
                }
            }
        } else {
            perror("child exit");
            exit(1);
        }
    }

    close(fdl[0]);
    close(fdr[0]);
    
    *pcount = num_forks;

    double d = (dl < dr) ? dl : dr;
    // return combine_lr(P, n, P[p_mid], d);
    double dlr = combine_lr(P, n, P[p_mid], d);
    return (dlr < d) ? dlr : d;
}

double closest_parallel(struct Point P[], size_t n, int pdmax, int *pcount)
{
    qsort(P, n, sizeof(struct Point), compare_x);
    return _closest_parallel(P, n, pdmax, pcount);
}

