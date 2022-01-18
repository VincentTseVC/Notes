
#include <stdio.h>
#include <string.h>

typedef struct record {
    char name[30];
    short yob;
} Record;   // 32 bytes


int get_yob(FILE *f, const char *name, short *pyob) {
    // reset the file pointer to the first byte 
    fseek(f, 0, SEEK_SET);

    Record rcd;

    // fread return the number of item it reads.
    while (fread(&rcd, sizeof(Record), 1, f) == 1) {
        if (strcmp(rcd.name, name) == 0) {
            *pyob = rcd.yob;
            return 1;
        }
    }
    return 0;
}

void set_yob(FILE *f, const char *name, short yob) {
    // reset the file pointer
    fseek(f, 0, SEEK_SET);
    
    Record rcd;
    while (fread(&rcd, sizeof(Record), 1, f) == 1) {
        if (strcmp(rcd.name, name) == 0) {
            // change the year in the file.
            fseek(f, -2, SEEK_CUR);
            fwrite(&yob, sizeof(short), 1, f);
            return;
        }
    }
    strcpy(rcd.name, name);
    rcd.yob = yob;
    fwrite(&rcd, sizeof(Record), 1, f);
}

int main(int argc, char **argv) {
    // defualt filename
    char *filename = "records";
    // given filename
    if (argc == 2) filename = argv[1];

    FILE *f;
    if ((f = fopen(filename, "w+")) == NULL) {
        fprintf(stderr, "failed to open");
        return 1;
    }


    set_yob(f, "Vincent", 1995);
    set_yob(f, "Paco", 200);
    set_yob(f, "Brian", 300);

    
    short yob;
    if (get_yob(f, "Vincent", &yob)) 
        printf("Vincent yob: %d\n", yob);
    else
        printf("Vincent is not found..\n");

    if (get_yob(f, "Brian", &yob)) 
        printf("Brian yob: %d\n", yob);
    else
        printf("Brian is not found..\n");

    if (get_yob(f, "Paco", &yob)) 
        printf("Paco yob: %d\n", yob);
    else
        printf("Paco is not found..\n");


    set_yob(f, "Paco", 1999);


     if (get_yob(f, "Paco", &yob)) 
        printf("Paco yob: %d\n", yob);
    else
        printf("Paco is not found..\n");


    return 0;
}