#include <stdio.h>
#include "average.h"


int main() {
    double arr[] = {5.0, 6.0, 7.0, 8.0};

    double result = average(4, arr);

    printf("The average of 5, 6, 7 and 8 is pretty cool: %.4f\n", result);
    return 0;
}

# Changed the numbers to 5-8, added coolness
