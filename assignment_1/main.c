#include <stdio.h>
#include "calculator.h"

int main() {
    double num1 = 10.0, num2 = 5.0;
    
    // Calculate the result
    double result = add(divide(num1, num2), subtract(multiply(num1, num2), num1));
    
    // Print the result for verification
    printf("Result: %lf\n", result);
    
    // Return the result as an exit code
    return (int)result;
}
