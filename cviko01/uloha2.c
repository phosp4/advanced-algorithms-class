#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#define MAX_BUFFER_LEN 100

int main()
{
    char buffer[MAX_BUFFER_LEN];
    bzero(buffer, MAX_BUFFER_LEN);

    fflush(stdout);
    fgets(buffer, MAX_BUFFER_LEN, stdin);

    for (uint16_t i = 0; i < atoi(buffer); i++) {
        
    }

    // char *ret = fgets(buffer, MAX_BUFFER_LEN, stdin);

    // if (ret == NULL) {
    //     printf("Input error");
    //     return EXIT_FAILURE;
    // }

    for (uint16_t i = 0; i < atoi(buffer); i++) {
        printf("adsf \n");
    }
}