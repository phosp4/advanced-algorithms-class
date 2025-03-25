// prva fungujuca verzia
// v com boli (mohli byt) chyby:
//  - male datove typy, pozorne sledovat maxima co su v zadani
//  - nepresne datove typy - int, long, namiesto uintXX
//  - najdolezitejsie - vsetko velke musi byt dynamicky alokovane (vsetky polia)
//  - nakoniec pomohlo generovanie vlastneho vstupu velkeho a grok.com

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <stdint.h>
#include <inttypes.h>
#define MAX_OUTS 500000
#define MAX_VAL 1000000000
#define MIN_VAL 0

typedef struct {
    uint64_t min;
    uint64_t max;
} result_t;

uint64_t max(uint64_t a, uint64_t b)
{
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

uint64_t min(uint64_t a, uint64_t b)
{
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

void update_tree_value(uint64_t min_tree[], uint64_t max_tree[], uint64_t orig_idx, uint64_t val, uint64_t n)
{
    uint64_t idx = orig_idx + n;
    min_tree[idx] = val;
    max_tree[idx] = val;

    uint64_t new_min_val;
    uint64_t new_max_val;

    while (idx > 1) {
        idx = idx / 2;
        new_min_val = min(min_tree[2 * idx], min_tree[(2 * idx) + 1]);
        new_max_val = max(max_tree[2 * idx], max_tree[(2 * idx) + 1]);

        if ((min_tree[idx] == new_min_val) && (max_tree[idx] == new_max_val)) {
            break;
        }
        
        min_tree[idx] = new_min_val;
        max_tree[idx] = new_max_val;
    }
}

uint64_t get_tree_max(uint64_t max_tree[], uint64_t start, uint64_t end, uint64_t n)
{
    start += n;
    end += n;
    uint64_t max_val = MIN_VAL;

    while (start < end) {
        if (start % 2 == 1) {
            max_val = max(max_val, max_tree[start]);
            start++;
        }
        if (end % 2 == 1) {
            end--;
            max_val = max(max_val, max_tree[end]);
        }
        
        start = start / 2;
        end = end / 2;
    }

    return max_val;
}

uint64_t get_tree_min(uint64_t min_tree[], uint64_t start, uint64_t end, uint64_t n)
{
    start += n;
    end += n;
    uint64_t min_val = MAX_VAL;

    while (start < end) {
        if (start % 2 == 1) {
            min_val = min(min_val, min_tree[start]);
            start++;
        }
        if (end % 2 == 1) {
            end--;
            min_val = min(min_val, min_tree[end]);
        }
        
        start = start / 2;
        end = end / 2;
    }

    return min_val;
}

int main()
{
    uint64_t n;
    scanf("%" SCNu64, &n);
    
    // Dynamically allocate arr on the heap
    uint64_t *arr = malloc(n * sizeof(uint64_t));
    if (!arr) {
        fprintf(stderr, "Memory allocation for arr failed\n");
        return 1;
    }

    for (uint64_t i = 0; i < n; i++) {
        scanf("%" SCNu64, &arr[i]);
    }

    uint64_t *min_tree = malloc(2 * n * sizeof(uint64_t));
    uint64_t *max_tree = malloc(2 * n * sizeof(uint64_t));
    if (!min_tree || !max_tree) {
        fprintf(stderr, "Memory allocation for trees failed\n");
        free(arr);
        if (min_tree) free(min_tree);
        if (max_tree) free(max_tree);
        return 1;
    }

    bzero(min_tree, 2 * n * sizeof(uint64_t));
    bzero(max_tree, 2 * n * sizeof(uint64_t));    

    for (uint64_t i = 0; i < n; i++) {
        min_tree[i + n] = arr[i];
        max_tree[i + n] = arr[i];
    }

    for (uint64_t i = n - 1; i > 0; i--) {
        min_tree[i] = min(min_tree[2 * i], min_tree[(2 * i) + 1]);
        max_tree[i] = max(max_tree[2 * i], max_tree[(2 * i) + 1]);
    }

    char sign;
    uint64_t idx1, idx2;

    // Dynamically allocate outs on the heap
    result_t *outs = malloc(MAX_OUTS * sizeof(result_t));
    if (!outs) {
        fprintf(stderr, "Memory allocation for outs failed\n");
        free(arr);
        free(min_tree);
        free(max_tree);
        return 1;
    }
    uint64_t out_count = 0;

    while (1) {
        scanf(" %c", &sign);
        if (sign == '-') {
            break;
        }
        
        scanf("%" SCNu64 " %" SCNu64, &idx1, &idx2);

        if (sign == '.') {
            update_tree_value(min_tree, max_tree, idx1 - 1, idx2, n);
        }
        if (sign == '?') {
            result_t out;
            out.min = get_tree_min(min_tree, idx1 - 1, idx2, n);
            out.max = get_tree_max(max_tree, idx1 - 1, idx2, n);
            outs[out_count] = out;
            out_count++;
        }
    }

    for (uint64_t i = 0; i < out_count; i++) {
        printf("%" PRIu64 " %" PRIu64 "\n", outs[i].min, outs[i].max);
    }
    
    // Free all dynamically allocated memory
    free(arr);
    free(min_tree);
    free(max_tree);
    free(outs);

    return 0;
}