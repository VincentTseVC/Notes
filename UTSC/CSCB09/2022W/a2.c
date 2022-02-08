#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct variable {
  char *name;
  char *scope;
  char *type;
  size_t size;
  struct variable *next;
} Var;

typedef struct scope {
  char *name;
  int num_lines;
  int num_variables;
  struct scope *next;
} Scope;

Var *create_var(char *name, char *scope, char *type, size_t size) {
  Var *var = malloc(sizeof(Var));
  var->name = malloc(sizeof(char) * (strlen(name) + 1));
  var->scope = malloc(sizeof(char) * (strlen(scope) + 1));
  var->type = malloc(sizeof(char) * (strlen(type) + 1));

  strcpy(var->name, name);
  strcpy(var->scope, scope);
  strcpy(var->type, type);
  var->size = size;
  var->next = NULL;

  return var;
}

Scope *create_scope(char *name) {
  Scope *scope = malloc(sizeof(Scope));
  scope->name = malloc(sizeof(char) * (strlen(name) + 1));
  strcpy(scope->name, name);
  scope->num_lines = 0;
  scope->num_variables = 0;
  scope->next = NULL;
  return scope;
}


char *strip(char *s) {
  int i = 0;
  for (; s[i] == ' '; i++);
  // strcpy(s, s+i);
  return s + i;
}

int declaring_vars(char *line) {
  return (strncmp(line, "int", 3) == 0 || 
          strncmp(line, "float", 5) == 0 || 
          strncmp(line, "char", 4) == 0);
}

size_t get_size(char *type) {
  if (strstr(type, "*"))          return sizeof(void *);
  if (strcmp(type, "int") == 0)   return sizeof(int);
  if (strcmp(type, "float") == 0) return sizeof(float);
  if (strcmp(type, "char") == 0)  return sizeof(char);
  return 0;
}


void display_memory(char *address_space, Var *head) {
  printf("### %s ###\n", address_space);
  for (Var *curr=head->next; curr != NULL; curr=curr->next) {
    printf("   %s\t%s\t%s\t%zu\n", 
      curr->name, curr->scope, curr->type, curr->size);
  }
  printf("\n");
}


int main(int argc, char **argv) {
  
  if (argc != 2) return 1;
  char *src_file = argv[1];

  FILE *f;
  if ((f = fopen(src_file, "r")) == NULL) {
    perror("failed to open file\n");
    return 1;
  } 

  // ROData (read only string literal)
  Var *ro_head = create_var("", "", "", 0); // dummy
  Var *ro_tail = ro_head;

  // static (global variables)
  Var *static_head = create_var("", "", "", 0); // dummy
  Var *static_tail = static_head;

  // heap
  Var *heap_head = create_var("", "", "", 0); // dummy
  Var *heap_tail = heap_head;

  // unused space
  Var *unused_head = create_var("", "", "", 0); // dummy
  Var *unused_tail = unused_head;

  // stack (function variables)
  Var *stack_head = create_var("", "", "", 0); // dummy
  Var *stack_tail = stack_head;

  Var *new_var;
  char *varname, *scope, *type;
  size_t size;

  // ------------------

  char buff[1024];
  char line[1024];
  int len;

  int open = 0;


  Scope *global_scope = create_scope("global");
  Scope *curr_scope = global_scope;
  int num_scope = 0;

  char *funcname;

  char *left_b, *space, *token;

  while (fgets(buff, 1023, f) != NULL) {
    global_scope->num_lines += 1;

    // TODO: change place
    if (curr_scope != global_scope && open != 0)
      curr_scope->num_lines += 1;

    // strip the leading white space
    strcpy(line, strip(buff));
    len = strlen(line);
    line[len-1] = '\0';
    len--;

    // skip some lines 
    if (len == 0) continue; // blank line
    if (line[0] == '/') continue; // in-line comment
    // if (line[0] == '*' && line[len-1] != ';') continue; // block comment

    
    if      (line[0] == '{') open += 1;
    else if (line[0] == '}') open -= 1;

    // function header, loop, if statements
    else if (line[len-1] == ')') {
      /**
       *    space left_b
       *       |    |
       *    int main(int argc, char** argv)
       *        |   0
       *    funcname
       */


      // if (open != 0) continue;
      printf("%s\n", line);
      left_b = strchr(line, '(');
      space = strchr(line, ' ');
      // if (left_b - space == 1) continue; // loop syntax

      // get function name
      funcname = space + 1;
      *left_b = '\0';

      // create scope
      curr_scope->next = create_scope(funcname);
      curr_scope = curr_scope->next;
      num_scope += 1;


      // parameters
      token = strtok(left_b+1, " ");
      while (token != NULL) {
        type = token;
        size = get_size(type);
        varname = strtok(NULL, " ");
        varname[strlen(varname)-1] = '\0'; // remove ',' or ')'

        new_var = create_var(varname, curr_scope->name, type, size);
        stack_tail->next = new_var;
        stack_tail = new_var;
        curr_scope->num_variables += 1;

        token = strtok(NULL, " ");
      }

    }

    // variables
    else if (declaring_vars(line)) {
      
      line[strlen(line)-1] = '\0'; // remove ';'

      /* split the line by " " */
      // Extract the first token
      type = strtok(line, " ");
      size = get_size(type);

      // loop through the string to extract all varnames
      varname = strtok(NULL, " ");
      while (varname != NULL) {
        // TODO: fix pointers & array

        // create new variable and append to the end of scope list
        new_var = create_var(varname, curr_scope->name, type, size);

        if (curr_scope == global_scope) {
          static_tail->next = new_var;
          static_tail = new_var;
        } else {
          stack_tail->next = new_var;
          stack_tail = new_var;
        }

        curr_scope->num_variables += 1;

        varname = strtok(NULL, " ");
      }
    }
    printf("%s", line); // debug
  }


  if (fclose(f) != 0) {
    perror("failed to close file\n");
    return 1;
  }
  
  
  printf(">>> Memory Model Layout <<<\n\n");
  printf("***  exec // text ***\n");
  printf("   %s\n\n", src_file);
  
  printf("### ROData ###\t\tscope\ttype\tsize\n");
  // 
  printf("\n");
  
  display_memory("static data", static_head);
  display_memory("heap", heap_head);
  display_memory("unused space", unused_head);
  display_memory("stack", stack_head);


  printf("**** STATS ****\n");
  printf("   - Total number of lines in the file: %d\n", global_scope->num_lines);
  printf("   - Total number of functions: %d\n", num_scope);
  printf("     ");
  int i;
  Scope *curr;
  for (i = 0, curr=global_scope->next; curr != NULL; i++, curr=curr->next)
    printf("%s%s", i == 0 ? "" : ", ", curr->name);
  printf("\n");

  printf("   - Total number of lines per functions:\n");
  for (curr=global_scope->next; curr != NULL; curr=curr->next)
    printf("     %s: %d\n", curr->name, curr->num_lines);

  printf("   - otal number of variables per function:\n");
  for (curr=global_scope->next; curr != NULL; curr=curr->next)
    printf("     %s: %d\n", curr->name, curr->num_variables);

  printf("//////////////////////////////\n");
  return 0;
}