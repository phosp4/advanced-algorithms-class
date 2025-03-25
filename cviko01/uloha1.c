#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#define MAX_BUFFER_LEN 100

int main()
{
    char buffer[MAX_BUFFER_LEN];
    bzero(buffer, MAX_BUFFER_LEN);

    fflush(stdout);

    char *ret = fgets(buffer, MAX_BUFFER_LEN, stdin);

    if (ret == NULL) {
        printf("Input error");
        return EXIT_FAILURE;
    }

    printf("Hello world!\n");
}