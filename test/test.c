#include <stdio.h>

int main() {
    // Declare a character array to store the user's name
    char name[100];

    // Prompt the user to enter their name
    printf("Enter your name: ");
    // Read the user's input and store it in the 'name' array
    scanf("%s", name);
    // Print a greeting using the entered name
    printf("Hello, %s! Welcome to the world of C programming.\n", name);
    // Prompt the user to enter their name
    printf("Enter your name: ");
    // Read the user's input and store it in the 'name' array
    scanf("%s", name);
    // Print a greeting using the entered name
    printf("Hello, %s! Welcome to the world of C programming.\n", name);
    return 0; // Indicate successful execution to the operating system
}