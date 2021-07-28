/**
 * CSC A48 - Intro to Computer Science II, Summer 2020
 * 
 * Assignment 3 - Graffit
 * 
 * Graphs &
 * Recursion
 * Assignment
 * For
 * Freshmen
 * In
 * Toronto
 *
 * (I am so proud of that initialism.)
 * 
 * This is the program file where you will implement your solution for
 * assignment 3. Please make sure you read through this file carefully
 * and that you understand what is provided and what you need to complete.
 * 
 * You will also need to have read the handout carefully. 
 * 
 * Parts where you have to implement functionality are clearly labeled TODO
 * 
 * Be sure to test your work thoroughly, our testing will be extensive
 * and will check that your solution is *correct*, not only that it
 * provides functionality.
 * 
 * (c) 2020 William Song, Mustafa Quraish
 **/

#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_STR_LEN 1024
#ifndef __testing
#define MAT_SIZE 3	// A small graph
#endif

typedef struct user_struct {
    char name[MAX_STR_LEN];
    struct friend_node_struct* friends;
    struct brand_node_struct* brands;
    bool visited;
} User;

typedef struct friend_node_struct {
    User* user;
    struct friend_node_struct* next;
} FriendNode;

typedef struct brand_node_struct {
    char brand_name[MAX_STR_LEN];
    struct brand_node_struct* next;
} BrandNode;

/** Note: We are reusing the FriendNode here as a Linked List for allUsers.
  * This is usually bad coding practice but it will allow us to reuse the
  * helper functions.
  **/
FriendNode* allUsers; 

int brand_adjacency_matrix[MAT_SIZE][MAT_SIZE];
char brand_names[MAT_SIZE][MAX_STR_LEN];

/**
 * Checks if a user is inside a FriendNode LL.
 **/
bool in_friend_list(FriendNode *head, User *node) {
  for (FriendNode *cur = head; cur != NULL; cur = cur->next) {
    if (strcmp(cur->user->name, node->name) == 0) {
      return true;
    }
  }
  return false;
}

/**
 * Checks if a brand is inside a BrandNode LL.
 **/
bool in_brand_list(BrandNode *head, char *name) {
  for (BrandNode *cur = head; cur != NULL; cur = cur->next) {
    if (strcmp(cur->brand_name, name) == 0) {
      return true;
    }
  }
  return false;
}

/**
 * Inserts a User into a FriendNode LL in sorted position. If the user 
 * already exists, nothing is done. Returns the new head of the LL.
 **/
FriendNode *insert_into_friend_list(FriendNode *head, User *node) {
  if (node == NULL) return head;

  if (in_friend_list(head, node)) {
    printf("User already in list\n");
    return head;
  }
  FriendNode *fn = calloc(1, sizeof(FriendNode));
  fn->user = node;
  fn->next = NULL;

  if (head == NULL)
    return fn;
    
  if (strcmp(head->user->name, node->name) > 0) {
    fn->next = head;
    return fn;
  } 

  FriendNode *cur;
  for (cur = head; cur->next != NULL && strcmp(cur->next->user->name, node->name) < 0;
       cur = cur->next)
    ;
  fn->next = cur->next;
  cur->next = fn;
  return head;
}

/**
 * Inserts a brand into a BrandNode LL in sorted position. If the brand 
 * already exists, nothing is done. Returns the new head of the LL.
 **/
BrandNode *insert_into_brand_list(BrandNode *head, char *node) {
  if (node == NULL) return head;

  if (in_brand_list(head, node)) {
    printf("Brand already in list\n");
    return head;
  }
  BrandNode *fn = calloc(1, sizeof(BrandNode));
  strcpy(fn->brand_name, node);
  fn->next = NULL;

  if (head == NULL)
    return fn;
    
  if (strcmp(head->brand_name, node) > 0) {
    fn->next = head;
    return fn;
  } 

  BrandNode *cur;
  for (cur = head; cur->next != NULL && strcmp(cur->next->brand_name, node) < 0;
       cur = cur->next)
    ;
  fn->next = cur->next;
  cur->next = fn;
  return head;
}

/**
 * Deletes a User from FriendNode LL. If the user doesn't exist, nothing is 
 * done. Returns the new head of the LL.
 **/
FriendNode *delete_from_friend_list(FriendNode *head, User *node) {
  if (node == NULL) return head;

  if (!in_friend_list(head, node)) {
    printf("User not in list\n");
    return head;
  }

  if (strcmp(head->user->name, node->name) == 0) {
    FriendNode *temp = head->next;
    free(head);
    return temp;
  }

  FriendNode *cur;
  for (cur = head; cur->next->user != node; cur = cur->next)
    ;

  FriendNode *temp = cur->next;
  cur->next = temp->next;
  free(temp);
  return head;
}

/**
 * Deletes a brand from BrandNode LL. If the user doesn't exist, nothing is 
 * done. Returns the new head of the LL.
 **/
BrandNode *delete_from_brand_list(BrandNode *head, char *node) {
  if (node == NULL) return head;

  if (!in_brand_list(head, node)) {
    printf("Brand not in list\n");
    return head;
  }

  if (strcmp(head->brand_name, node) == 0) {
    BrandNode *temp = head->next;
    free(head);
    return temp;
  }

  BrandNode *cur;
  for (cur = head; strcmp(cur->next->brand_name, node) != 0; cur = cur->next)
    ;

  BrandNode *temp = cur->next;
  cur->next = temp->next;
  free(temp);
  return head;
}

/**
 * Prints out the user data.
 **/
void print_user_data(User *user) {
  printf("User name: %s\n", user->name);
  printf("Friends:\n");
  for (FriendNode *f = user->friends; f != NULL; f = f->next) {
    printf("   %s\n", f->user->name);
  }
  printf("Brands:\n");
  for (BrandNode *b = user->brands; b != NULL; b = b->next) {
    printf("   %s\n", b->brand_name);
  }
}

/**
 * Get the index into brand_names for the given brand name. If it doesn't
 * exist in the array, return -1
 **/
int get_brand_index(char *name) {
  for (int i = 0; i < MAT_SIZE; i++) {
    if (strcmp(brand_names[i], name) == 0) {
      return i;
    }
  }
  printf("brand '%s' not found\n", name);
  return -1; // Not found
}

/**
 * Print out brand name, index and similar brands.
 **/
void print_brand_data(char *brand_name) {
  int idx = get_brand_index(brand_name);
  if (idx < 0) {
    printf("Brand '%s' not in the list.\n", brand_name);
    return;
  }
  printf("Brand name: %s\n", brand_name);
  printf("Brand idx: %d\n", idx);
  printf("Similar brands:\n");
  for (int i = 0; i < MAT_SIZE; i++) {
    if (brand_adjacency_matrix[idx][i] == 1 && strcmp(brand_names[i], "") != 0) {
      printf("   %s\n", brand_names[i]);
    }
  }
}

/**
 * Read from a given file and populate a the brand list and brand matrix.
 **/
void populate_brand_matrix(char* file_name) {
    // Read the file
    char buff[MAX_STR_LEN];
    FILE* f = fopen(file_name, "r");
    fscanf(f, "%s", buff);
    char* line = buff;
    // Load up the brand_names matrix
    for (int i = 0; i < MAT_SIZE; i++) {
        if (i == MAT_SIZE - 1) {
            strcpy(brand_names[i], line);
            break;
        }
        int index = strchr(line, ',') - line;
        strncpy(brand_names[i], line, index);
        line = strchr(line, ',') + sizeof(char);
    }
    // Load up the brand_adjacency_matrix
    for (int x = 0; x < MAT_SIZE; x++) {
        fscanf(f, "%s", buff);
        for (int y = 0; y < MAT_SIZE; y++) {
            int value = (int) buff[y*2];
            if (value == 48) { value = 0; }
            else {value = 1;}
            brand_adjacency_matrix[x][y] = value;
        }
    }
}


// Users
/**TODO: Complete this function
 * Creates and returns a user. Returns NULL on failure.
 **/
User* create_user(char* name) {
  User *node = NULL;
  if ((node = (User *) calloc(1, sizeof(User))) == NULL) return NULL; 

  strcpy(node->name, name);
  node->friends = NULL;
  node->brands = NULL;
  node->visited = false;

  if (in_friend_list(allUsers, node) == true) {
    free(node);
    return NULL;
  }
  allUsers = insert_into_friend_list(allUsers, node);
  return node;
}

/**TODO: Complete this function
 * Deletes a given user. 
 * Returns 0 on success, -1 on failure.
 **/
int delete_user(User* user) {

  if (in_friend_list(allUsers, user) == false) return -1;
  allUsers = delete_from_friend_list(allUsers, user);
  for (FriendNode *curr = user->friends; curr != NULL; curr = curr->next) 
    curr->user->friends = delete_from_friend_list(curr->user->friends, user);
  free(user);
  return 0;
}

/**TODO: Complete this function
 * Create a friendship between user and friend.
 * Returns 0 on success, -1 on failure.
 **/
int add_friend(User* user, User* friend) {
  if (in_friend_list(user->friends, friend) == true) return -1;
  user->friends = insert_into_friend_list(user->friends, friend);
  friend->friends = insert_into_friend_list(friend->friends, user);
  return 0;
}

/**TODO: Complete this function
 * Removes a friendship between user and friend.
 * Returns 0 on success, -1 on faliure.
 **/
int remove_friend(User* user, User* friend) {
  if (in_friend_list(user->friends, friend) == false) return -1;
  user->friends = delete_from_friend_list(user->friends, friend);
  friend->friends = delete_from_friend_list(friend->friends, user);
  return 0;
}

/**TODO: Complete this function
 * Creates a follow relationship, the user follows the brand.
 * Returns 0 on success, -1 on faliure.
 **/
int follow_brand(User* user, char* brand_name) {
  if (get_brand_index(brand_name) == -1) return -1;
  if (in_brand_list(user->brands, brand_name)) return -1;
  user->brands = insert_into_brand_list(user->brands, brand_name);
  return 0;
}

/**TODO: Complete this function
 * Removes a follow relationship, the user unfollows the brand.
 * Returns 0 on success, -1 on faliure.
 **/
int unfollow_brand(User* user, char* brand_name) {
  if (get_brand_index(brand_name) == -1) return -1;
  if (in_brand_list(user->brands, brand_name) == false) return -1;
  user->brands = delete_from_brand_list(user->brands, brand_name);
  return 0;
}

/**TODO: Complete this function
 * Return the number of mutual friends between two users.
 **/
int get_mutual_friends(User* a, User* b) {
  int count = 0;
  for (FriendNode *curr= a->friends; curr != NULL; curr = curr->next)
    count += in_friend_list(b->friends, curr->user) ? 1 : 0;
  return count;
}


void reset_visited(User* users[], int N) {
  for (int i = 0; i < N; i++) users[i]->visited = false;
}

int get_num_users() {
  int num_users = 0;
  for (FriendNode *curr = allUsers; curr != NULL; curr=curr->next, num_users++)
    ;
  return num_users;
}


/**TODO: Complete this function
 * A degree of connection is the number of steps it takes to get from
 * one user to another.
 * 
 * For example, if X & Y are friends, then we expect to recieve 1 when calling
 * this on (X,Y). Continuing on, if Y & Z are friends, then we expect to
 * recieve 2 when calling this on (X,Z).
 * 
 * Returns a non-negative integer representing the degrees of connection
 * between two users, -1 on failure.
 **/
int get_degrees_of_connection(User* a, User* b) {
  if (in_friend_list(allUsers, a) == false || in_friend_list(allUsers, b) == false) return -1;

  if (a == b) return 0;

  int path[get_num_users()];
  User* queue[get_num_users()];
  int front = 0, back = 0;

  path[back] = 0;

  queue[back++] = a;
  a->visited = true;

  for (User *curr = queue[front]; front != back; curr = queue[++front]) {
    for (FriendNode *fcurr = curr->friends; fcurr != NULL; fcurr = fcurr->next) {
      if (fcurr->user->visited) continue;
      if (fcurr->user == b) {
        reset_visited(queue, back);
        return path[front] + 1;
      }
      fcurr->user->visited = true;
      path[back] = path[front] + 1;
      queue[back++] = fcurr->user;
    }
  }
  reset_visited(queue, back);
  return -1;
}


// Brands
/**TODO: Complete this function
 * Marks two brands as similar.
 **/
void connect_similar_brands(char* brandNameA, char* brandNameB) {
  int brandNameA_idx = get_brand_index(brandNameA);
  if (brandNameA_idx == -1) return;
  int brandNameB_idx = get_brand_index(brandNameB);
  if (brandNameB_idx == -1) return;

  brand_adjacency_matrix[brandNameA_idx][brandNameB_idx] = 1;
  brand_adjacency_matrix[brandNameB_idx][brandNameA_idx] = 1;
}

/**TODO: Complete this function
 * Marks two brands as not similar.
 **/
void remove_similar_brands(char* brandNameA, char* brandNameB) {
  int brandNameA_idx = get_brand_index(brandNameA);
  if (brandNameA_idx == -1) return;
  int brandNameB_idx = get_brand_index(brandNameB);
  if (brandNameB_idx == -1) return;

  brand_adjacency_matrix[brandNameA_idx][brandNameB_idx] = 0;
  brand_adjacency_matrix[brandNameB_idx][brandNameA_idx] = 0;
}



// Harder ones
/**TODO: Complete this function
 * Returns a suggested friend for the given user, returns NULL on failure.
 * See the handout for how we define a suggested friend.
 **/
User* get_suggested_friend(User* user) {
  
  User* suggested_friend = NULL;

  int max_common_brands = -1;

  int common_brands;

  for (FriendNode *curr = allUsers; curr != NULL; curr = curr->next) {
    if (curr->user == user || in_friend_list(user->friends, curr->user)) continue;

    common_brands = 0;
    for (BrandNode *bcurr = curr->user->brands; bcurr != NULL; bcurr = bcurr->next) 
      if (in_brand_list(user->brands, bcurr->brand_name))
        common_brands++;
    
    if (common_brands >= max_common_brands) {
      max_common_brands = common_brands;
      suggested_friend = curr->user;
    }
  }

  return suggested_friend;
}

/**TODO: Complete this function
 * Friends n suggested friends for the given user.
 * See the handout for how we define a suggested friend.
 * Returns how many friends were successfully followed.
 **/
int add_suggested_friends(User* user, int n) {
  if (n < 1) return 0;
  if (!in_friend_list(allUsers, user)) return 0;

  int count = 0;
  for (int i = 0; i < n; i++) {
    User *suggest_friend = get_suggested_friend(user);
    if (suggest_friend == NULL) break;
    add_friend(user, suggest_friend);
    count += 1;
  }
  return count;
}

char *get_suggested_brand_name(User *user) {
  int similar_count[MAT_SIZE];
  memset(arr, 0, sizeof(arr));

  // for (int i = 0; i < MAT_SIZE; i++)
  //   arr[i] = 0; // initialize every count to be ZERO

  for (BrandNode *bcurr = user->brands; bcurr != NULL; bcurr = bcurr->next) {
    int row = get_brand_index(bcurr->brand_name);
    for (int col = 0; col < MAT_SIZE; col++) {
      if (in_brand_list(user->brands, brand_names[col]))
        similar_count[col] = -10;
      if (brand_adjacency_matrix[row][col] == 1)
        similar_count[col] += 1;
    }
  }

  char *suggested_brand_name = NULL;
  int max_count = -1;
  int count;
  char *brand_name;
  for (int i = 0; i < MAT_SIZE; i++) {

    count = similar_count[i];
    brand_name = brand_names[i];
    // found a new highest count (new most similar) [UPDATE]
    if (count > max_count) {
      max_count = count;
      suggested_brand_name = brand_name;
    }
    // founda a SAME highest count [ONLY UPDATE IF new brand name is larger]
    else if (count == max_count) {
      if (strcmp(suggested_brand_name, brand_name) < 0)
        suggested_brand_name = brand_name;
    }
  }

  return suggested_brand_name;
}

/**TODO: Complete this function
 * Follows n suggested brands for the given user.
 * See the handout for how we define a suggested brand.     
 * Returns how many brands were successfully followed. 	  	
 **/
int follow_suggested_brands(User* user, int n) {
  if (n < 1) return 0;
  if (!in_friend_list(allUsers, user)) return 0;
  int count = 0;
  for (int i = 0; i < n; i++)  {
    char *suggested_brand_name = get_suggested_brand_name(user);
    if (suggested_brand_name == NULL) break;
    follow_brand(user, suggested_brand_name);
    count += 1;
  }
  return count;
}
