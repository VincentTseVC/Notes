


#include <stdio.h>

int main() {

    int x;

    FILE *f;
    if ((f = fopen("a.txt", "r+")) == NULL) {
        // perror("Cannot open...\n");
        fprintf(stderr, "Cannot open ...\n");
        return 1;   // <--- error
    }

    // char s[10];
    // while (fscanf(stdin, "x -> %d", &x) != EOF) {
    //     fprintf(stdout ,"%d\n", x);
    // }

    // char c;
    // while ((c = getc(f)) != EOF) {
    //     printf("%c\n", c);
    // }



    char name[20];

    fgets(name, 20, f);
    printf("%s\n", name);

    fputs("Vincent", f);




    return 0; // <--- exit successfully
}